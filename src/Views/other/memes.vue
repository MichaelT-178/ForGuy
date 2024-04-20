<template>
    <div class="meme-page">
        <h1>{{ text.page }}</h1>
        <p>{{ text.desc }}</p>
        
        <div class="meme-container" v-for="(meme, index) in memeObjects" :key="index">
            <div class="meme-text">{{ index + 1 }}. {{ meme.text }}</div>
            <div class="image-container">
                <img :src="meme.image" alt="Meme Picture">
                <span class="hidden-text">{{ meme.transcription }}</span>
            </div>
        </div>
    </div>
</template>


<script setup>
import { ref } from 'vue';
import { memeObjects } from "../../components/Memes.vue"
import AllData from "../../data/Other/Memes.json";

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];

</script>


<style scoped>
.meme-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.meme-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 400px;
    margin-bottom: 35px;
}

.meme-text {
    font-size: 18px;
}

.image-container {
    position: relative;
    width: 400px;
}

.hidden-text {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: -1;
    pointer-events: none;
    color: transparent;
    background: transparent;
    border: none;
}

img {
    width: 100%;
    border: 2px solid black;
    margin-top: 8px;
    display: block;
}

p {
    margin-top: -15px;
    font-size: 20px;
}
</style>
