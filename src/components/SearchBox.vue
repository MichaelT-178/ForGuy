<template>
    <div v-if="showBox" class="modal">
      <div class="modal-content">
        <div class="content-container">
          <slot>
            <span style="color: black">HELLO</span>
          </slot> 
          <router-link 
              v-for="item in searchMenu" 
              :key="item.title" 
              :to="item.link" 
              @click="closeModal">
              {{ item.title }}
           </router-link>
          <button @click="closeModal">Close</button>
          <button @click="printJSON">Data</button>
        </div>
      </div>
    </div>
  </template>
  
<script setup>
import { ref, defineProps, defineEmits, watchEffect } from 'vue';
import SearchData from '../data/SearchData.json';

const props = defineProps({
  isOpen: Boolean
});
  
const emits = defineEmits(['update:isOpen']);
const showBox = ref(props.isOpen);
  
const closeModal = () => {
  showBox.value = false;
  emits('update:isOpen', false);
};
  
watchEffect(() => {
  showBox.value = props.isOpen;
});

const jsonData = ref(SearchData);
const searchMenu = jsonData.value;

const printJSON = () => {
  console.log(JSON.parse(JSON.stringify(searchMenu)))
}

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
  
  .modal-content {
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  }
  
  .content-container {
    display: flex;
    flex-direction: column;
    align-items: center; 
    gap: 10px; 
  }
  </style>
  