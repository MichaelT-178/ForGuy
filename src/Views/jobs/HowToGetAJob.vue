<template>
    <h1 class="job-header">How to get a job</h1>
    <div v-for="(tip, index) in tips" :key="tip.Name" class="tip-section">
        <p class="tip-text">Tip {{ index + 1 }}: {{ tip.Name }}</p>
        <AccordionMenu :item="tip" :isOpen="allOpen"/>
        <p style="margin-bottom: 35px;"></p>
    </div>
    <p style="margin-bottom: 60px;"></p>
</template>


<script setup>
import { ref } from 'vue';
import HowToGetAJobData from "../../data/jobs/HowToGetAJob.json";
import AccordionMenu from "../../components/AccordionMenu.vue";

const jsonData = ref(HowToGetAJobData);
const tips = jsonData.value["Tips"];
const allOpen = ref(false);

</script>

<style scoped>

.job-header {
    margin-left: auto; /* Ensures it aligns with the start of the accordion if necessary */
    margin-right: auto; /* Ensures it aligns with the start of the accordion if necessary */
    width: 80%; /* Matches the accordion menu width for alignment */
}


.tip-section {
    margin-bottom: 20px; /* Adjusts spacing between each tip section */
}

.tip-text {
    margin-left: auto; /* Ensures it aligns with the start of the accordion if necessary */
    margin-right: auto; /* Ensures it aligns with the start of the accordion if necessary */
    width: 80%; /* Matches the accordion menu width for alignment */
    margin-bottom: 10px; /* Spacing between the tip text and the accordion menu */
    font-size: 20px;
    font-weight: 600;
    color: darkblue;
}



</style>