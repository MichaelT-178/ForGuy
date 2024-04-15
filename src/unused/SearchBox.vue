<template>
  <div v-if="showBox" class="modal">
    <div class="modal-content">
        <div class="modal-header">
          <h2 class="search-title">Search</h2>
          <span class="material-icons" @click="closeModal">close</span>
        </div>
      <div class="content-container">
        <input type="text" v-model="searchString" placeholder="Lookup Term..." class="search-bar" />
        <span class="search-label">Search Term Appears In...</span>
        <div class="search-results">
          <div
            v-for="item in filteredSearchMenu"
            :key="item.id"
            class="search-item"
            >
            <router-link :to="item.link" @click="closeModal">
              {{ item.MenuName }}
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watchEffect } from 'vue';
import SearchPages from '../data/SearchPages.json';

const props = defineProps({
  isOpen: Boolean
});

const emits = defineEmits(['update:isOpen']);
const showBox = ref(props.isOpen);
const searchString = ref('');

const closeModal = () => {
  showBox.value = false;
  searchString.value = "";
  emits('update:isOpen', false);
};

watchEffect(() => {
  showBox.value = props.isOpen;
});

const jsonData = ref(SearchPages);
const searchMenu = jsonData.value;

const filteredSearchMenu = computed(() => {
  return searchMenu.filter(item => item.AllText.toLowerCase().includes(searchString.value.toLowerCase().trim()));
});

// const printJSON = () => {
//   console.log(JSON.parse(JSON.stringify(searchMenu)))
// }
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
}

.modal-header {
  background-color: teal;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}

.search-title {
  color: white;
  margin: 0;
  font-size: 20px;
}

.close-icon {
  color: white;
  cursor: pointer;
  font-size: 24px;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  width: 300px;
  height: 400px;
}

.content-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.search-bar {
  padding: 10px;
  margin-bottom: 10px;
  margin-top: 10px;
  width: 80%;
  border: 2px solid #626262;
  border-radius: 5px;
}

.search-label {
  color: black;
  align-self: flex-start;
}

.search-results {
  overflow-y: auto;
  max-height: 260px;
  width: 100%;
  scrollbar-width: thin;
  scrollbar-color: hsl(0, 0%, 0%) transparent;
}

.search-results::-webkit-scrollbar {
  width: 8px;
}

.search-results::-webkit-scrollbar-thumb {
  background-color: #5B5B5B;
  border-radius: 4px;
}

.search-item {
  background-color: #fff;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  margin-bottom: 10px;
  text-align: left;
  cursor: pointer; 
}

.search-item:hover {
  background-color: #EEEEEE;
  border-color: #ccc; 
}

.search-item a {
  color: black;
  text-decoration: none;
  display: block; 
}

.material-icons:hover {
  color: #ffd483;
}


</style>