<template>
    <h1 class="job-header">Computer Science Minor</h1>
    <p class="job-description" v-html="createHyperLink(description)"></p>
    <div v-for="course in classes" :key="course.Name" class="class-section">
        <p class="class-text">{{ course.Name }} <span v-html="course.Elective" style="color: purple"></span></p>
        <AccordionMenu :item="course" :isOpen="allOpen"/>
        <p style="margin-bottom: 35px;"></p>
    </div>
    <p style="margin-bottom: 100px;"></p>
    <h1 class="job-header">Computer Science Major</h1>
    <p class="job-description" v-html="createHyperLink(descriptionTwo)"></p>
    <div v-for="course in semesterClasses" :key="course.Name" class="class-section">
        <p class="class-text">{{ course.Name }}</p>
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
const descriptionTwo = jsonData.value["DescriptionTwo"];
const semesterClasses = jsonData.value["SemesterClasses"];

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

.class-section {
    margin-bottom: 20px;
    margin-left: 9px;
    margin-right: 9px;

}

.class-text {
    margin-left: auto;
    margin-right: auto;
    width: 80%;
    margin-bottom: 10px;
    font-size: 20px;
    font-weight: 600;
    color: #000062;
}


/* OTHER */
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

.tip-section {
    margin-bottom: 5px;
    width: 575px;
}

.tip-text {
    position: relative;
    width: auto;
    font-size: 21px;
    font-weight: 500;
}

.tip-text::before {
    content: attr(data-index);
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: darkblue;
    color: white;
    border-radius: 50%;
    width: 25px;
    height: 25px;
    margin-left: -35px;
    position: absolute;
    top: 0;
    transform: translateY(-50%);
    font-size: 14px;
}

.text-section {
    font-size: 19.5px;
    word-wrap: break-word; 
    overflow-wrap: break-word; 
    margin-top: -13px;
}

@media (max-width: 700px) {
    .tip-header {
        width: 490px;
    }
    
    .description {
        width: 490px;
    }

    .tip-section {
        width: 375px;
    }
}

</style>