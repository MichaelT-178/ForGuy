ChatGPT 4

User
<template>
  <div class="menu-overlay">
    <div class="header">
      <span class="views-text">Views</span>
      <span class="material-icons close-icon" @click="closeMenu">close</span>
    </div>
    <div v-for="(menuItem, index) in menuItems" :key="index" class="menu-item">
      <div @click="menuItem.route ? navigateTo(menuItem.route) : toggleSubMenu(index)" class="menu-text">
        <span v-if="menuItem.icon" class="material-icons menu-icon" :class="{ 'active-text': activeIndex === index }">{{ menuItem.icon }}</span>
        <span :class="{ 'active-text': activeIndex === index }">{{ menuItem.text }}</span>
        <span v-if="menuItem.subMenu" class="material-icons expand-icon" @click.stop="toggleSubMenu(index)" :class="{ 'active-icon': activeIndex === index }">
          {{ activeIndex === index ? 'expand_less' : 'expand_more' }}
        </span>
      </div>
      <div v-if="menuItem.subMenu && activeIndex === index" class="sub-menu">
        <div v-for="(subItem, subIndex) in menuItem.subMenu" :key="subIndex" @click.stop="navigateTo(subItem.link)">
          <span class="material-icons" style="margin-right: 8.5px">{{ subItem.icon }}</span>
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
  closeMenu(); // Closes the menu when a link is navigated to
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
  padding: 20px;
  width: calc(100% - 40px);
}

.views-text {
  font-size: 30px;
  color: #ffd483;
}

.close-icon {
  cursor: pointer;
  font-size: 30px;
  color: white;
}

.close-icon:hover {
  color: red;
}

.menu-item {
  color: white;
  cursor: pointer;
  border-top: 0.85px solid white;
  border-bottom: 0.85px solid white;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.menu-text:hover {
  background-color: #00C0C0;
}

.menu-text {
  display: flex;
  align-items: center;
  padding: 10px 20px;
  font-size: 1.5em;
  /* width: 90.23%; */
  width: 100%;
}

.material-icons.menu-icon, .expand-icon {
  margin-right: 10px;
}

.active-text, .active-icon {
  color: #ffd483; /* Highlights text and expand icon in yellow when active */
}

.expand-icon {
  transition: transform 0.3s;
  font-size: 30px;
  margin-left: auto;
  margin-right: 0px;
}

.sub-menu {
  /* width: 95.1%; */
  width: 100%;
  background-color: rgba(255, 255, 255, 0.1);
  padding: 5px 0px 5px 20px;
}

.sub-menu:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.sub-menu div {
  display: flex;
  align-items: center;
  font-size: 1em;
  padding: 5px 0;
  margin-bottom: 6px;
}

.sub-menu div:hover {
  color: #ffd483;
}

</style>
