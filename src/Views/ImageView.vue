<template>
  <div class="container">
    <div class="content">
      <div class="text-content">
        <h1 class="pic-name">{{ info.Name }}</h1>
        <p class="description" v-html="highlightLinkText(info.Description)"></p>
      </div>
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

const highlightLinkText = (text) => {
  const urlPattern = /(\b(https?|ftp|file):\/\/|www\.)[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|]/ig;

  return text.replace(urlPattern, (url) => 
    {
      const realURL = !url.startsWith("http") ? `https://${url}` : url;

      return `<a href="${realURL}" target="_blank" 
                style="color: #007AFF; text-decoration: none;" 
                onmouseover="this.style.color='blue'; this.style.textDecoration='underline';" 
                onmouseout="this.style.color='#007AFF'; this.style.textDecoration='none';"
              >
              ${url}</a>`;
    }
  );
};

</script>


<style scoped>

.container {
  display: flex;
  justify-content: center; 
  width: 100%;
  height: 100vh;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 700px;
}

.text-content {
  text-align: left;
  width: 100%;
}

.description {
  margin-top: -12px;
  font-size: 18px;
}

.picture {
  border: 1.5px solid #000000;
  width: 700px; 
  max-height: 900px;
  overflow-y: auto;
  margin-top: -5px;
  margin-bottom: 60px;
}

</style>
