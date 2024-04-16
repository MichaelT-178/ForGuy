<template>
    <router-link :to="resultPage.Link" class="no-style-link">
        <div class="search-card">
            <h2 class="title"><span>{{ resultPage.Title }}</span></h2>
            
            <div v-for="result in resultPage.MatchedResults" :key="result.title">
                <div v-for="(value, key) in result" :key="key">
                    <div v-html="value"></div>
                </div>
            </div>

        </div>
    </router-link>
</template>


<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  resultPage: {
    type: Object,
    required: true,
    default: () => ({})
  }
});

</script>


<style scoped>

.search-card {
    padding: 0px 0px 10px 30px; /* Top, right, bottom, left */
    border: 1px solid #ccc;
    border-radius: 8px;
    width: 600px;
    margin: 20px auto;
    position: relative;
    overflow: hidden;
    background: white;
    border-top: 2px solid darkblue; 
    border-bottom: 2px solid darkblue; 
    transition: background-color 0.3s;
}
  
.search-card:hover {
    border-top: 2px solid red;
    border-bottom: 2px solid red;
    cursor: pointer;
}

.search-card:hover .title span {
    color: red; /* This line changes the text color */
}

.no-style-link {
    text-decoration: none; 
    color: inherit; 
    display: inline;
}

.title span {
    border-bottom: 1px solid #ccc;
    padding-bottom: 1px;
    display: inline-block;
    padding-right: 110px;
}

.title {
    margin-bottom: 20px;
}

.search-card div {
    margin-bottom: 7px;
}

.search-card p {
    padding: 0px 15px 0px 0px;
}

@media (max-width: 700px) {
    .search-card {
        width: 425px;
    }

    .title span {
        padding-right: 48px;
    }
}

</style>

  
  
  