<template>
    <h1>Apps To Download</h1>
    <p class="description">These are phone apps that I'd recommend doing. I chose them based on how useful and enjoyable they are to use.</p>
    <button @click="toggleAll" class="expand-all-btn">{{ allOpen ? 'Close All' : 'Expand All' }}</button>
    <div class="app-section">
        <h2>Apps To Download</h2>
        <p>These are apps that I think would be worth downloading. <a :href="emailStr" class="email-btn">Email yourself all these download links.</a></p>
        <div class="app-menu">
            <div v-for="app in appsToDownload" :key="app.Name" class="app-item">
                <AccordionMenu :item="app" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <div class="app-section">
        <h2>Apps You've Probably Already Downloaded</h2>
        <p>These are popular apps that you have probably already downloaded.</p>
        <div class="app-menu">
            <div v-for="app in appsProbablyDownloaded" :key="app.Name" class="app-item">
                <AccordionMenu :item="app" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <p style="margin-bottom: 100px;"></p>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import AllData from "../../data/other/AppsToDownload.json";
import AccordionMenu from "../../components/AccordionMenu.vue";
import { bodyContent } from "../../components/AppEmail.vue";

const jsonData = ref(AllData);
const appsToDownload = jsonData.value["AppsToDownload"];
const appsProbablyDownloaded = jsonData.value["Kinda Obviously"];
const allOpen = ref(false);


const emailTo = ""; //TODO
const subject = "All the App Download Links";
const emailStr = `mailto:${emailTo}?subject=${subject}&body=${bodyContent}`;


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

.app-section {
    margin-bottom: 55px;
}

.app-menu {
    margin-top: -5px;
}

.app-item {
    margin-bottom: 12px;
}

.email-btn {
    color: #007AFF;
    cursor: pointer;
    text-decoration: none;
}

.email-btn:hover {
    color: #0000D7;
    text-decoration: underline;
}

</style>