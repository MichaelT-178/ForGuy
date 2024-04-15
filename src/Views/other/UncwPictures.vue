<template>
    <div class="uncw-pics-page">
        <h1>{{ text.page }}</h1>
        <p>{{ text.desc }}</p>
        
        <div class="uncw-pics-container" v-for="(pic, index) in uncwPics" :key="index">
            <div class="uncw-pic-text">{{ index + 1 }}. {{ pic.text }}</div>
            <img :src="pic.image" alt="Uncw Picture">
        </div>
        
        <h1>{{ text.header2 }}</h1>
        <p>{{ text.desc2 }}</p>
        
        <div class="uncw-pics-container" v-for="(pic, index) in NorthCarolinaPics" :key="index">
            <div class="uncw-pic-text">{{ index + 1 }}. {{ pic.text }}</div>
            <img :src="pic.image" alt="Uncw Picture">
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { uncwPics, NorthCarolinaPics } from "../../components/UncwPics.vue";
import AllData from "../../data/Other/UncwPics.json";

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];

</script>

<style scoped>
.uncw-pics-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.uncw-pics-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 400px;
    margin-bottom: 35px;
}

.uncw-pic-text {
    font-size: 18px;
}

img {
    width: 400px;
    border: 2px solid black;
    margin-top: 8px;
}

p {
    margin-top: -15px;
    font-size: 20px;
}

</style>
