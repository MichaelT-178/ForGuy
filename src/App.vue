<template>
  <div class="app">
    <component :is="isMobile ? MenuBarTwo : Menu" />
    <router-view />
  </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import Menu from './components/MenuBar.vue';
import MenuBarTwo from './components/MenuBarTwo.vue';

const isMobile = ref(window.innerWidth <= 700);

const updateWindowSize = () => {
  isMobile.value = window.innerWidth <= 700;
};

onMounted(() => {
  window.addEventListener('resize', updateWindowSize);
});

onUnmounted(() => {
  window.removeEventListener('resize', updateWindowSize);
});

</script>


<style>

body, html {
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
}

img {
  width: 100%; 
  height: auto;
  display: block;
}

</style>