<template>
  <div>
    <div class="search-bar-container">
      <div class="input-icon-container">
        <span class="material-icons">
          search
        </span>
        <!-- Search bar -->
        <input type="text" 
               v-model="searchQuery" 
               placeholder="Search by name or term..." 
               :class="{'rounded-top': searchQuery, 'rounded-all': !searchQuery}"
               @keydown.enter="handleEnterPress"
        >
        <span class="material-icons" id="close-icon" @click="closeSearchBar">close</span>
      </div>

      <!-- Search Results -->
      <div v-if="filteredResults.length" class="results">
        <router-link 
          v-for="(result, index) in filteredResults" 
          :key="index" 
          :to="result.Link" 
          class="result-item" 
          @click="closeSearchBar"
        >
          <span class="emoji"> {{ result.Emoji }} </span>
          {{ result.MenuName }}
        </router-link>
      </div>
      <!-- No Results but query entered -->
      <div v-else-if="searchQuery && !filteredResults.length" class="results">
        <div class="result-item" @click="goToResultsPage">
          <!-- <span class="emoji">🔍</span> -->
          Press <span style="color: #7A008D">return/enter</span> to see results for "{{ searchQuery }}"
        </div>
      </div>
      
    </div>
  </div>
</template>


<script setup>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import SearchData from '../data/SearchData.json'; 

const searchQuery = ref('');
const filteredResults = ref([]);
const emit = defineEmits(['close-search']);
const router = useRouter();

const goToResultsPage = () => {
  emit('close-search');
  router.push({ name: 'SearchResults', params: { SearchQuery: searchQuery.value } });
};

const handleEnterPress = (event) => {
  if (event.key === 'Enter') {
    goToResultsPage();
  }
};

const filterResults = () => {
  if (searchQuery.value) {
    filteredResults.value = SearchData.filter((item) =>
      item.MenuName.toLowerCase().includes(searchQuery.value.toLowerCase())
    ).slice(0, 11); //Only 11 results show at a time.
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
  border-radius: 19px;
  z-index: 2;
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
  background-color: #F9F9F9;
}

.results {
  position: absolute;
  top: 100%;
  width: 100.1%;
  background-color: white;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  z-index: 100;
  border-radius: 0 0 19px 19px;
  overflow: hidden;
  background-color: #00C0C0;
}

.emoji {
  font-size: 19px;
  margin-right: 4.85px;
}

.result-item {
  display: block;
  padding: 10px 15px;
  color: black;
  text-decoration: none;
  text-align: left;
  line-height: 1; 
}

.result-item:hover {
  background-color: #ffd483;
  color: #333;
  border-radius: 4px;
  cursor: pointer;
  /* border-left: 3px solid darkblue; */
}

.rounded-top {
  border-radius: 19px 19px 0 0;
}

.rounded-all {
  border-radius: 19px;
}

#close-icon {
  position: absolute;
  cursor: pointer; 
  pointer-events: auto; 
  right: 4.75px; 
  color: #757575; 
  padding: 10px;
  font-size: 23.5px;
}

#close-icon:hover {
  color: #B91212;
}

</style>

  