<template>
    <h1>VSCode Extensions</h1>
    <p class="description">When you click on a link it will take you to a website. To download the extension just click the green "install" button and it will open in VSCode.</p>
    <button @click="toggleAll" class="expand-all-btn">{{ allOpen ? 'Close All' : 'Expand All' }}</button>
    <div class="extension-section">
        <h2>VSCode Extensions</h2>
        <p>These are VSCode Extensions that I think would be worth downloading. <a :href="emailStr" class="email-btn">Email yourself all these download links.</a></p>
        <div class="extension-menu">
            <div v-for="extension in extensions" :key="extension.Name" class="extension-item">
                <AccordionMenu :item="extension" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <p style="margin-bottom: 100px;"></p>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import AllData from "../../data/CompSci/VSCodeExtensions.json";
import AccordionMenu from "../../components/AccordionMenu.vue";
import { bodyContent } from "../../components/ExtensionEmail.vue";

const jsonData = ref(AllData);
const extensions = jsonData.value["Extensions"];
const allOpen = ref(false);


const emailTo = ""; //TODO
const subject = "VSCode Extension Download Links";
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

.extension-section {
    margin-bottom: 55px;
}

.extension-menu {
    margin-top: -5px;
}

.extension-item {
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