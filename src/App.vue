<template>
  <div class="app">
    <Menu />

    <router-view />
  </div>
</template>

<script setup>
import Menu from './components/MenuBar.vue';

//activeSubMenuIndex === index && showMenu 

//https://fonts.google.com/icons

</script>


<style>
    /* Ensure no space at the top */
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