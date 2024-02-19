<template>
    <h1>Offers I've Recieved</h1>
    <p class="description">{{ description }}</p>
    <div class="job-section">
        <h2>Internship Offers</h2>
        <p>These are the Internship Offers I have recieved.</p>
        <div class="job-menu">
            <div v-for="internship in internships" :key="internship.Name" class="job-item">
                <AccordionMenu :item="internship" />
            </div>
        </div>
    </div>
    <div class="job-section">
        <h2>Full-Time Offers</h2>
        <p>These are the full-time Offers I have recieved.</p>
        <div class="job-menu">
            <div v-for="job in fullTimeJobs" :key="job.Name" class="job-item">
                <AccordionMenu :item="job" />
            </div>
        </div>
    </div>
    <div class="job-section">
        <h2>Companies Where I interviewed</h2>
        <p>These are the companies where I got an interview, but not an offer for various reasons.</p>
        <div class="job-menu">
            <div v-for="interview in interviews" :key="interview.Name" class="job-item">
                <AccordionMenu :item="interview" />
            </div>
        </div>
    </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import AllData from "../../data/jobs/OffersRecieved.json";
import AccordionMenu from "../../components/AccordionMenu.vue";

const jsonData = ref(AllData);
const description = jsonData.value["description"];
const internships = jsonData.value["internships"];
const fullTimeJobs = jsonData.value["fullTime"];
const interviews = jsonData.value["interviews"];

onMounted(() => {
  document.body.style.backgroundColor = 'white';
  document.documentElement.style.backgroundColor = 'white';
});

onUnmounted(() => {
  document.body.style.backgroundColor = '';
  document.documentElement.style.backgroundColor = '';
});

</script>


<style scoped> 

h1, h2 {
    text-align: left;
    margin-left: 9.5%;
}

.description {
    margin-bottom: 32px;
}

p {
    text-align: left;
    margin-left: 9.5%;
    margin-top: -15px;
    font-size: 18px;
    width: 80%; 
}

.job-section {
    margin-bottom: 55px;
}

.job-menu {
    margin-top: -5px;
}

.job-item {
    margin-bottom: 13px;
}

</style>