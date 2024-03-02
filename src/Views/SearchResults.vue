<template>
    <div>
      <p>Search results for: "{{ searchQuery }}"</p>
    </div>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue';
  import { useRoute } from 'vue-router';
  
  const route = useRoute();

  const searchQuery = ref(route.params.SearchQuery);
  
  watch(() => route.params.SearchQuery, (newSearchQuery) => {
    searchQuery.value = newSearchQuery;
  });
  </script>
  
  