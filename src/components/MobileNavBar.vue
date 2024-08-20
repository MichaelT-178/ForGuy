<template>
  <div class="top-menu">

    <div class="overlay" v-if="isMenuOpen" @click="closeMenu"></div>
    <div class="search-overlay" v-if="isSearchBarOpen" @click="closeSearchBar"></div>

    <span class="material-icons menu-icon" v-if="!isSearchBarOpen" @click="toggleMenu">
      menu
    </span>

    <SideBar v-if="isMenuOpen" @close-menu="isMenuOpen = false"/>

    <div v-if="isSearchBarOpen" class="search-bar-wrapper">
      <SearchBar @close-search="closeSearchBar"></SearchBar>
    </div>

    <span class="material-icons search-icon" v-if="!isMenuOpen && !isSearchBarOpen" @click="toggleSearchBar">
      search
    </span>
  </div>
</template>


<script setup>
import { ref } from 'vue';
import SearchBar from './MobileSearchBar.vue';
import SideBar from './SideBar.vue';

const isSearchBarOpen = ref(false);
const isMenuOpen = ref(false);

const toggleSearchBar = () => {
  isSearchBarOpen.value = !isSearchBarOpen.value;

  if (isSearchBarOpen.value) {
    isMenuOpen.value = false;
  }
};

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;

  if (isMenuOpen.value) {
    isSearchBarOpen.value = false;
  }
};

const closeMenu = () => {
  isMenuOpen.value = false;
};

const closeSearchBar = () => {
  isSearchBarOpen.value = false;
};

</script>


<style scoped>
.overlay {
  position: fixed;
  left: 0;
  width: 100vw;
  height: 200vh;
  background-color: rgba(0, 0, 0, 0.6);
  z-index: 1;
}

.search-overlay {
  position: fixed;
  top: 60.2px;
  left: 0;
  width: 100vw;
  height: calc(100vh - 40px);
  background-color: rgba(0, 0, 0, 0.6);
  z-index: 10;
}

.top-menu {
  background-color: teal;
  padding: 10px 20px;
  min-height: 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  z-index: 15;
}

.search-bar-wrapper {
  position: fixed;
  top: 40px;
  left: 50%;
  transform: translateX(-50%);
  width: calc(100vw - 40px);
  margin-top: -30px;
  z-index: 20;
}

.material-icons {
  transform: translateY(5.1px);
  color: #fff;
  cursor: pointer;
  font-size: 27px;
}

.material-icons:hover {
  color: #ffd483;
}

.menu-icon {
  margin-left: 3px;
  margin-top: -9px;
}

.search-icon {
  margin-right: 3px;
  margin-top: -9px;
}

</style>
