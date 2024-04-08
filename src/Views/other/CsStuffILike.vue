<template>
    <div class="container">
        <h1>CS Stuff I like</h1>
        <p>This is the CS Stuff I like page. Note the them being used for the code blocks is Atom Dark One.</p>

        <h2 class="gh-header-two" ref="createGHAccount">How to Create a GitHub Account</h2>
        <p class="description-two">These are instructions to setup Git and create a GitHub account.</p>

        <div v-for="point in csStuff" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(point.description)"></span>
            </p>
        </div>

        <div v-for="code in codeSyntax" :key="code.Name" class="code-blocks">
            <CodeBlock :codeInfo="code"></CodeBlock>
        </div>
    </div>
</template>


<script setup>
import { ref } from 'vue';
import AllData from '../../data/Other/CsStuffILike.json';
import CodeBlock from '../../components/Code/CodeBlock.vue';
import { createHyperLink } from "../../components/FormatLinks.vue";


const jsonData = ref(AllData);

const csStuff = jsonData.value["CsStuff"];


const codeSyntax = jsonData.value["Code"];

</script>

<style scoped>

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.bullet-pt {
    display: flex;
    align-items: flex-start;
    margin-top: -10px;
    margin-left: 20px;
    margin-bottom: 24px;
    font-size: 19px;
    width: 690px;
}

.bullet-pt-span {
    background-color: darkblue;
    border-radius: 50%;
    color: white;
    font-size: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 24px;
    height: 24px;
    min-width: 24px;
    margin-right: 10px;
    user-select: none;
    margin-bottom: 10px;
}

.gh-header-two {
    text-align: left;
    width: 690px;
}

.description-two {
    margin-top: -15px;
    font-size: 19px;
    width: 690px;
}

@media (max-width: 700px) {
    .gh-header-two {
        width: 490px;
    }

    .description-two {
        width: 490px;
    }
}

</style>