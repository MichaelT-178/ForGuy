<template>
    <div>
      <header>
        <div class="top-menu" @mouseover="showMenu = true" @mouseout="hideMenu">
          <div class="menu-items">  
            <div
              class="menu-item"
              v-for="(menuItem, index) in menuItems"
              :key="index"
              @mouseover="menuItem.subMenu ? showSubMenu(index) : null; 
                          hoveredOver = menuItem.subMenu ? true : false"

              @mouseout="menuItem.subMenu ? hideSubMenu : null; 
                         hoveredOver = false"   
              @click="handleMenuClick(menuItem)"
            >
              <span>{{ menuItem.text }}
                <i class="material-icons" :style="{ opacity: menuItem.subMenu ? 1 : 0, width: menuItem.subMenu ? 1 : 0 }">
                  {{ activeSubMenuIndex === index && hoveredOver && menuItem.subMenu ? 'expand_less' : 'expand_more' }}
                </i>
              </span>
              <div
                class="sub-menu"
                v-if="menuItem.subMenu"
                v-show="showMenu && activeSubMenuIndex === index"
                @mouseover="showSubMenu(index)"
                @mouseout="hideSubMenu"
              >
                <ul>
                  <li v-for="(subMenuItem, subIndex) in menuItem.subMenu" :key="subIndex">
                    <a :href="subMenuItem.link">{{ subMenuItem.text }}</a>
                  </li>
                </ul>
              </div>
            </div>
            <span 
              class="material-icons" 
              @click="isSearchBox = true" 
              style="flex-shrink: 0; margin-top: 3.2px">
              search
            </span>
          </div>
          <SearchBox v-model:isOpen="isSearchBox">
          </SearchBox>
        </div>
      </header>
    </div>
</template>
  
<script setup>
import { ref } from 'vue';
import router from '../router';
import SearchBox from './SearchBox.vue';
import { menuItems } from './MenuItems.vue';

const showMenu = ref(false);
const activeSubMenuIndex = ref(null);
const hoveredOver = ref(false);

const isSearchBox = ref(false);
  
const showSubMenu = (index) => {
  activeSubMenuIndex.value = index;
}

const hideSubMenu = () => {
  activeSubMenuIndex.value = null;
}

const hideMenu = () => {
  showMenu.value = false;
}

const handleMenuClick = (menuItem) => {
  if (menuItem.route) {
    router.push(menuItem.route);
  }
}

</script>

<style scoped>

.top-menu {
  background-color: teal;
  color: #fff;
  padding: 10px 0;
}

.menu-items {
  display: flex;
  justify-content: space-between;
  max-width: 800px;
  margin: 0 auto;
}

.menu-item {
  position: relative;
  cursor: pointer;
  /* padding: 10px 15px; top right bottom left*/
  padding: 2.5px 11px 10px 14px;
  transition: background-color 0.3s ease;
}

.menu-item:hover {
  background-color: #555;
}

.sub-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: teal;
  padding: 10px;
  border-radius: 0 0 5px 5px;
  z-index: 1;
}

.menu-item:hover .sub-menu {
  display: block;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 5px;
}

a {
  text-decoration: none;
  color: #fff;
}

a:hover {
  text-decoration: underline;
}

.material-icons {
  transform: translateY(5.1px); 
}



</style>
  