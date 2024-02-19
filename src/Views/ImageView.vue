<template>
  <div class="container">
    <div class="content">
      <h1 class="pic-name">{{ info.Name }}</h1>
      <p class="description">{{ info.Description }}</p>
      <img :src="imagePath" :alt="info.Name" class="picture"/>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();

const info = {
  Name: route.params.Name,
  Description: route.params.Description,
  Pic: route.params.Pic,
};

const imagePath = new URL(`../assets/${info.Pic}`, import.meta.url).href;
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center; /* Center the content block */
  width: 100%;
}

.description {
  margin-top: -17px;
  font-size: 18px;
}

.content {
  text-align: left; /* Align text to the left */
  display: flex;
  flex-direction: column;
  align-items: flex-start; /* Align items to the start (left) */
}

.picture {
  border: 1.5px solid #000000;
  width: 700px; /* Adjust based on your requirement */
  max-height: 800px;
  overflow-y: auto;
}
</style>
