<template>
    <div class="container">
        <h1 class="tip-header">Contacts</h1>
        <p class="description">These are useful job contacts from various companies.</p>
        <div class="tips-container">
            <div v-for="tip in tips" :key="tip.id" class="tip-section">
                <p class="tip-text" :data-index="tip.id"></p>
                <p class="text-section" v-html="tip.tip"></p>
            </div>
        </div>
        <p style="margin-bottom: 60px;"></p>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import AllData from "../../data/jobs/InterviewTips.json";

const jsonData = ref(AllData);
const tips = jsonData.value["Tips"];
</script>

<style scoped>

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.tip-header {
    text-align: left;
    border-bottom: 1.5px solid #d8dee4;
    padding-bottom: 7px;
    width: 690px;
}

.description {
    margin-top: -8px;
    font-size: 19px;
    width: 690px;
}

.tips-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

</style>
