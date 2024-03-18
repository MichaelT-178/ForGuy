<template>
    <h1 class="job-header">Computer Science Minor</h1>
    <p class="job-description" v-html="createHyperLink(description)"></p>
    <div v-for="course in classes" :key="course.Name" class="tip-section">
        <p class="tip-text">{{ course.Name }} <span v-html="course.Elective" style="color: purple"></span></p>
        <AccordionMenu :item="course" :isOpen="allOpen"/>
        <p style="margin-bottom: 35px;"></p>
    </div>
    <p style="margin-bottom: 80px;"></p>
</template>


<script setup>
import { ref } from 'vue';
import AllData from "../../data/Classes/CompSciMinor.json";
import AccordionMenu from "../../components/AccordionMenu.vue";
import { createHyperLink } from "../../components/FormatLinks.vue";

const jsonData = ref(AllData);
const description = jsonData.value["Description"];
const classes = jsonData.value["Classes"];

</script>


<style scoped>

.job-header {
    margin-left: auto;
    margin-right: auto;
    border-bottom: 1.5px solid #d8dee4;
    width: 80%;
}

.job-description {
    margin-left: auto;
    margin-right: auto;
    width: 79.5%;
    font-size: 20px;
    margin-top: -14px;
    margin-bottom: 25px;
}

.tip-section {
    margin-bottom: 20px;
    margin-left: 9px;
    margin-right: 9px;

}

.tip-text {
    margin-left: auto;
    margin-right: auto;
    width: 80%;
    margin-bottom: 10px;
    font-size: 20px;
    font-weight: 600;
    color: #000062;
}

</style>