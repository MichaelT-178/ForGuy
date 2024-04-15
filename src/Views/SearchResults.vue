
<template>
  <div class="container">
    <h1 class="search-header">Search Results</h1>
    <p class="description">The search term <span style="color: darkblue">"{{ searchQuery }}"</span> appears in the following pages.</p>

    <div v-for="contact in contacts" :key="contact.Company">
        <SearchCard :contact="contact"></SearchCard>
    </div>

    <p style="margin-bottom: 60px;"></p>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import SearchData from '../data/SearchData.json';
//import SearchData from '../components/data/SearchData.vue';
//#5943b6


//NEW DELETE
import AllData from "../data/LinkedIn/Contacts.json";
import SearchCard from "../components/SearchCard.vue"

const jsonData = ref(AllData);
const contacts = jsonData.value["Contacts"];
//NEW DELETE



const route = useRoute();

const searchQuery = ref(route.params.SearchQuery);
  
watch(() => route.params.SearchQuery, (newSearchQuery) => {
  searchQuery.value = newSearchQuery;
});

</script>


<style scoped>

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.search-header {
    text-align: left;
    border-bottom: 1.5px solid #d8dee4;
    padding-bottom: 7px;
    width: 690px;
}

.description {
    margin-top: -8px;
    font-size: 19px;
    width: 690px;
    margin-bottom: 4px;
}

@media (max-width: 700px) {

    .search-header {
        text-align: left;
        border-bottom: 1.5px solid #d8dee4;
        padding-bottom: 7px;
        width: 490px;
    }

    .description {
        width: 490px;
    }
}

</style>

  