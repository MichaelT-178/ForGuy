<template>
  <div class="search-bar-container">
    <div class="input-icon-container"> <!-- Add this container for input and icon -->
      <span class="material-icons">
        search
      </span>
      <input type="text" v-model="searchQuery" placeholder="Search term appears in..." :class="{'rounded-top': filteredResults.length, 'rounded-all': !filteredResults.length}">
    </div>
    <div v-if="filteredResults.length" class="results">
      <router-link v-for="(result, index) in filteredResults" :key="index" :to="result.link" class="result-item" @click="closeSearchBar">
        {{ result.MenuName }}
      </router-link>
    </div>
  </div>
</template>


<script setup>
import { ref, watch, defineEmits } from 'vue';
import SearchData from '../data/SearchData.json'; // Import your JSON data here

const searchQuery = ref('');
const filteredResults = ref([]);
const emit = defineEmits(['close-search']);

const filterResults = () => {
  if (searchQuery.value) {
    filteredResults.value = SearchData.filter((item) =>
      item.MenuName.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
  } else {
    filteredResults.value = [];
  }
};

const closeSearchBar = () => {
  emit('close-search');
};

watch(searchQuery, filterResults);

</script>


<style scoped>

.search-bar-container {
  position: relative;
  max-width: 500px;
  margin: auto;
  width: 80%;
  background-color: white;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  border-radius: 8px;
}

.input-icon-container {
  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
}

.material-icons {
  position: absolute;
  padding: 10px;
  color: #757575;
  pointer-events: none;
}

.search-bar-container input[type="text"] {
  width: 100%;
  height: 36px;
  padding: 0 15px;
  padding-left: 48px;
  font-size: 16px;
  border: none;
  background-color: #F3F3F3;
}

.results {
  position: absolute;
  top: 100%;
  width: 100%;
  background-color: white;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  z-index: 100;
  border-radius: 0 0 8px 8px;
  overflow: hidden;
}

.result-item {
  display: block;
  padding: 10px 15px;
  color: black;
  text-decoration: none;
  text-align: left;
}

.result-item:hover {
  background-color: #f0f0f0;
  color: #333;
  border-radius: 4px;
}

.rounded-top {
  border-radius: 8px 8px 0 0;
}

.rounded-all {
  border-radius: 8px;
}

</style>

  