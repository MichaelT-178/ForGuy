<template>
    <div class="container">
        <h1 class="tip-header">Computer Science Tips</h1>
        <p class="description">These are some more general tips I have for computer science.</p>
        <div class="tips-container">
            <div v-for="tip in tips" :key="tip.id" class="tip-section">
                <p class="tip-text" :data-index="tip.id"></p>
                <p class="text-section" v-html="processedTipContent(formatTip(tip))"></p>
            </div>
        </div>
        <p style="margin-bottom: 60px;"></p>
        <CodeBlock :codeInfo="shortcut" ref="codeBlockRef"></CodeBlock>
        <p style="margin-bottom: 100px;"></p>
        <CodeBlock :codeInfo="shortcut" ref="codeBlockTwoRef"></CodeBlock>
        <p style="margin-bottom: 60px;"></p>
    </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import AllData from "../../data/CompSci/CompSciTips.json";
import CodeBlock from '../../components/Code/CodeBlock.vue';

const jsonData = ref(AllData);
let tips = jsonData.value["Tips"];
const shortcut = jsonData.value["ComponentData"][0];

//Add refs here
const codeBlockRef = ref(null);
const codeBlockTwoRef = ref(null);
const codeBlockThreeRef = ref(null);


const scrollToRef = (refName) => {

    //Add refs here
    const refs = {
        codeBlockRef,
        codeBlockTwoRef,
        codeBlockThreeRef,
    };

    const targetElement = refs[refName]?.value?.$el;

    if (targetElement) {
        targetElement.scrollIntoView({ behavior: 'smooth' });
    } else {
        console.warn("No target element found for refName:", refName);
    }
}

const formatTip = (tip) => {
    return `<u>${tip.Underlined}</u>. ${tip.Tip}`;
}

const processedTipContent = (tip) => {
    return tip.replace(/Scroll down\((.*?)\)/g, (match, refName) => {
        return `<span href="#" class="scroll-down" data-ref-name="${refName}">Scroll down</span>`;
    });
}

onMounted(() => {
    document.querySelectorAll('.scroll-down').forEach(element => {
        element.addEventListener('click', (event) => {
            event.preventDefault();
            const refName = event.target.getAttribute('data-ref-name');
            scrollToRef(refName);
        });
    });
});

</script>


<style scoped>

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

:deep(.scroll-down) {
    text-decoration: none;
    color: blue;
    cursor: pointer;
}

:deep(.scroll-down:hover) {
    text-decoration: underline;
    color: darkblue;
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
