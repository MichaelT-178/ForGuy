<template>
    <h1>Useful Certifications</h1>
    <p class="description">{{ description }}</p>
    <button @click="toggleAll" class="expand-all-btn">{{ allOpen ? 'Close All' : 'Expand All' }}</button>
    <div class="job-section">
        <h2>Cloud Certifications</h2>
        <p>Cloud computing is a very popular, widely-used tool in software engineering these days. I think these certifications would greatly help you in basically any SWE job you get.</p>
        <div class="job-menu">
            <div v-for="cloudCert in cloudCertifications" :key="cloudCert.Name" class="job-item">
                <AccordionMenu :item="cloudCert" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <div class="job-section">
        <h2>Certifications for Essential Skills</h2>
        <p>These are certifications for very commonly used skills in software engineering jobs. I've been asked about my knowledge on these skills in basically every SWE interview I've done so far.</p>
        <div class="job-menu">
            <div v-for="skillCerts in skillCertifications" :key="skillCerts.Name" class="job-item">
                <AccordionMenu :item="skillCerts" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <div class="job-section">
        <h2>Machine Learning Certifications</h2>
        <p>Artificial Intelligence and Machine Learning are all the rage these days so I thought I'd add a section on it. I also feel like UNCW's AI concentration isn't the best way to learn real-world application of these skills and that a certification might be easier and more useful to get.</p>
        <div class="job-menu">
            <div v-for="mlCert in mlCertifications" :key="mlCert.Name" class="job-item">
                <AccordionMenu :item="mlCert" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <div class="job-section">
        <h2>Academic Certifications and Degrees</h2>
        <p>These are certifications and degrees from Universities that you might find helpful. I think having some form of education from another University can make up for the lack of "prestige" UNCW has.</p>
        <div class="job-menu">
            <div v-for="academicCert in academicCertifications" :key="academicCert.Name" class="job-item">
                <AccordionMenu :item="academicCert" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <div class="job-section">
        <h2>General Tips</h2>
        <p>These are general tips I have a for attaining certifications to make the most out of the experience and get the most value out of the certification itself. These tips might also make the process easier.</p>
        <div class="job-menu">
            <div v-for="tip in generalTips" :key="tip.Name" class="job-item">
                <AccordionMenu :item="tip" :isOpen="allOpen" />
            </div>
        </div>
    </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import AllData from "../../data/Classes/UsefulCertifications.json";
import AccordionMenu from "../../components/AccordionMenu.vue";

const jsonData = ref(AllData);
const description = jsonData.value["description"];
const cloudCertifications = jsonData.value["Cloud Certifications"];
const skillCertifications = jsonData.value["Certifications for Essential Skills"];
const mlCertifications = jsonData.value["Machine Learning Certifications"];
const academicCertifications = jsonData.value["Academic Certifications and Degrees"];
const generalTips = jsonData.value["GeneralTips"];

const allOpen = ref(false);

const toggleAll = () => {
    allOpen.value = !allOpen.value;
};

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

.expand-all-btn {
    padding: 5px 40px;
    border-radius: 5px;
    background-color: #007AFF;
    color: white;
    border: none;
    cursor: pointer;
    font-size: 16px;
    margin-left: 9.5%;
}

.expand-all-btn:hover {
    background-color: #0068DF;
}

h1, h2 {
    text-align: left;
    margin-left: 9.5%;
}

.description {
    margin-bottom: 20px;
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
    margin-bottom: 12px;
}

</style>