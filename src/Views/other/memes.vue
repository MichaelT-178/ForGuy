<template>
    <div class="meme-page">
        <h1>Memes</h1>
        <p>Computer Science Memes</p>
        
        <div class="meme-container" v-for="(meme, index) in memeObjects" :key="index">
            <div class="meme-text">{{ index + 1 }}. {{ meme.text }}</div>
            <img :src="meme.image" alt="Meme Picture">
        </div>
    </div>
</template>

<script setup>
import { memeObjects } from "../../components/Memes.vue"

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
