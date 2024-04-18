<template>
    <div class="menu-overlay">
      <div class="header">
        <span class="views-text">Views</span>
        <span class="material-icons close-icon" @click="closeMenu">close</span>
      </div>
      
      <div v-for="(menuItem, index) in menuItems" :key="index">
        <div @click="menuItem.route ? navigateTo(menuItem.route) : toggleSubMenu(index)" class="menu-item">
          <div class="menu-text">{{ menuItem.text }}</div>
        </div>
        <div v-if="menuItem.subMenu && activeIndex === index" class="sub-menu">
          <div v-for="(subItem, subIndex) in menuItem.subMenu" :key="subIndex" @click.stop="navigateTo(subItem.link)">
            <span class="material-icons">{{ subItem.icon }}</span>
            {{ subItem.text }}
          </div>
        </div>
      </div>
      
    </div>
  </template>
  
  
  
  <script setup>
  import { ref } from 'vue';
  import { menuItems } from './MenuItems.vue';
  import { useRoute, useRouter } from 'vue-router';
  
  const emit = defineEmits(['close-menu']);
  const router = useRouter();
  const activeIndex = ref(null);
  
  const closeMenu = () => {
    emit('close-menu');
  };
  
  const toggleSubMenu = (index) => {
    if (activeIndex.value === index) {
      activeIndex.value = null; // close if already open
    } else {
      activeIndex.value = index; // open the clicked menu
    }
  };
  
  const navigateTo = (link) => {
    router.push(link);
  };
  </script>
  
  

  <style scoped>
  .menu-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 80vw;
    height: 100vh;
    background-color: teal;
    z-index: 10;
    display: flex;
    flex-direction: column;
  }
  
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: calc(100% - 40px);
    padding: 20px;
  }
  
  .views-text {
    font-size: 30px;
    color: #ffd483;
  }
  
  .close-icon {
    cursor: pointer;
    font-size: 30px;
    color: white;
    margin-top: 3.85px;
  }
  
  .close-icon:hover {
    color: red;
  }
  
  .menu-item {
    color: white;
    cursor: pointer;
    border-top: 1px solid white;
    border-bottom: 1px solid white;
  }
  
  .menu-text {
    font-size: 1.5em;
    padding: 10px 20px;
  }
  
  .sub-menu {
    background-color: rgba(255, 255, 255, 0.1);
    padding-left: 20px;
  }
  
  .sub-menu div {
    display: flex;
    align-items: center;
    font-size: 0.9em;
  }
  
  .material-icons {
    margin-right: 10px;
  }
  </style>
  
  
  