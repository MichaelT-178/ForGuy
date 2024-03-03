<template>
    <h1>Class Recommendations</h1>
    <p class="description">These are classes and professors I really enjoyed taking or have heard good things about.</p>
    <button @click="toggleAll" class="expand-all-btn">{{ allOpen ? 'Close All' : 'Expand All' }}</button>
    <div class="item-section">
        <h2>Class Recommendations</h2>
        <p>These are classes I would recommend taking for various reasons.</p>
        <div class="item-menu">
            <div v-for="course in classes" :key="course.Name" class="item-item">
                <AccordionMenu :item="course" :isOpen="allOpen" />
            </div>
        </div>
    </div>
    <div class="item-section">
        <h2>Professor Recommendations</h2>
        <p>These are Professors I would recommend taking whenever possible.</p>
        <div class="item-menu">
            <div v-for="professor in professors" :key="professor.Name" class="item-item">
                <AccordionMenu :item="professor" :isOpen="allOpen" />
            </div>
        </div>
    </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import AllData from "../../data/Classes/ClassRecommendations.json";
import AccordionMenu from "../../components/AccordionMenu.vue";

const jsonData = ref(AllData);
const classes = jsonData.value["Classes"];
const professors = jsonData.value["Professors"];
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

.item-section {
    margin-bottom: 55px;
}

.item-menu {
    margin-top: -5px;
}

.item-item {
    margin-bottom: 12px;
}

</style>