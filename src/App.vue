<template>
  <div>
    <header>
      <div class="top-menu" @mouseover="showMenu = true" @mouseout="hideMenu">
        <div class="menu-items">
          <div
            class="menu-item"
            v-for="(menuItem, index) in menuItems"
            :key="index"
            @mouseover="showSubMenu(index)"
            @mouseout="hideSubMenu"
            @click="navigateToRoute(menuItem.route)"
          >
            <span>{{ menuItem.text }}</span>
            <div
              class="sub-menu"
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
        </div>
      </div>
    </header>
  </div>


  <router-view />

</template>

<script setup>
import { ref } from 'vue';

const showMenu = ref(false);
const activeSubMenuIndex = ref(null);

const menuItems = [
  {
    text: "Item 1",
    subMenu: [
      { text: "Home", link: "/" },
      { text: "About", link: "/about" },
    ],
  },
  {
    text: "Item 2",
    subMenu: [
      { text: "Subitem 2.1", link: "/subitem-2-1" },
      { text: "Subitem 2.2", link: "/subitem-2-2" },
      { text: "Subitem 2.3", link: "/subitem-2-3" },
    ],
  },
];

const showSubMenu = (index) => {
  activeSubMenuIndex.value = index;
}

const hideSubMenu = () => {
  activeSubMenuIndex.value = null;
}

const hideMenu = () => {
  showMenu.value = false;
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
  padding: 10px 15px;
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

</style>
