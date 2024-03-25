<template>
    <main class="about-page">
        <h1>CS Stuff I like</h1>
        <p>This is the CS Stuff I like page</p>

        <div v-for="code in codeSyntax" :key="code.Name" class="code-blocks">
            <CodeBlock :codeInfo="code"></CodeBlock>
        </div>
    </main>
</template>


<script setup>
import { ref } from 'vue';
import AllData from '../../data/Other/FavoriteCsStuff.json';
import CodeBlock from '../../components/Code/CodeBlock.vue';


const jsonData = ref(AllData);
const codeSyntax = jsonData.value["Code"];

</script>

<style scoped>
.code-blocks {
    margin-left: 100px;
}

</style>