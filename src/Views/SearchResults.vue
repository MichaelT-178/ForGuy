
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
import SearchCard from "../components/SearchCard.vue";
//import SearchData from '../components/data/SearchData.vue';
//#5943b6

const route = useRoute();

const searchQuery = ref(route.params.SearchQuery);
  
watch(() => route.params.SearchQuery, (newSearchQuery) => {
  searchQuery.value = newSearchQuery;
});


function highlightString(text, searchString) {
    let idx = 0;
    let highlightedText = '';
    const searchLength = searchString.length;
    const lowerText = text.toLowerCase();
    const lowerSearchString = searchString.toLowerCase();
    let count = 0;

    while (idx < text.length) {
        const nextFind = lowerText.indexOf(lowerSearchString, idx);

        if (nextFind === -1) {
            highlightedText += text.substring(idx);
            break;
        }

        highlightedText += text.substring(idx, nextFind) + `<span style="background-color: yellow">${text.substring(nextFind, nextFind + searchLength)}</span>`;
        idx = nextFind + searchLength;
        count++;
    }

    return { highlightedText, count };
}


function searchInResults(results, searchString) {
    const matchedResults = [];
    let totalHighlightCount = 0;

    results.forEach(result => {
        Object.entries(result).forEach(([key, value]) => {

            if (typeof value === 'string' && value.toLowerCase().includes(searchString.toLowerCase())) {
                const { highlightedText, count } = highlightString(value, searchString);
                matchedResults.push(`<p>${highlightedText}</p>`);
                totalHighlightCount += count;
            } else if (typeof value === 'number' && searchString === value.toString()) {
                matchedResults.push(`<p><span style="background-color: yellow">${value}</span></p>`);
                totalHighlightCount++;
            }

        });
    });

    return { matchedResults, totalHighlightCount };
}


function searchJson(data, searchString) {
    const allMatches = [];
    let totalCount = 0;

    data.forEach(item => {
        const results = item.Results || [];

        const { matchedResults, highlightCount } = searchInResults(results, searchString);

        if (matchedResults.length > 0) {
            allMatches.push({
                Title: item.Title,
                Link: item.Link,
                MatchedResults: matchedResults
            });
            totalCount += highlightCount;
        }

    });

    return { allMatches, totalCount };
}





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

  