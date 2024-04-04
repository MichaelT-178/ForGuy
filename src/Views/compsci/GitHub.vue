<template>
    <div class="container">
        <h1 class="gh-header">GitHub</h1>
        <p class="description">This is a description of GitHub and common commands.</p>
        <img src="../../assets/GitHub.png" alt="GitHub" class="github-pic"/>



        <h2 class="gh-header-two">What is GitHub and Git?</h2>
        <p class="description-two">How to get an existing folder onto GitHub.</p>



        <h2 class="gh-header-two">How to Create a GitHub Account</h2>
        <p class="description-two">These are instructions to setup Git and create a GitHub account.</p>

        <div v-for="point in setupGitHub" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>



        <h2 class="gh-header-two" ref="codeBlockRef">Existing Folder Commands</h2>
        <p class="description-two">How to get an existing folder onto GitHub.</p>


        <div v-for="point in existingFolderPts" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <CmdTable tableName="" :items="existingFolderCmds" class="cmd-table" ref="practiceTable"></CmdTable>
    </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import AllData from '../../data/CompSci/GitHub.json';
import CmdTable from "../../components/CommandTable.vue";
import { createHyperLink } from "../../components/FormatLinks.vue";
import CodeBlock from '../../components/Code/CodeBlock.vue';


const jsonData = ref(AllData);



const setupGitHub = jsonData.value["SetupGitHub"];


const existingFolderPts = jsonData.value["ExistingFolderPts"];
const existingFolderCmds = jsonData.value["ExistingFolder"];





//Add refs here
const codeBlockRef = ref(null);
// const codeBlockTwoRef = ref(null);
// const codeBlockThreeRef = ref(null);
// const codeBlockFourRef = ref(null);

// const secondSix = ref(null);
// const secondSeven = ref(null);
// const secondEight = ref(null);
// const secondTwentyOne = ref(null);
// const secondGitHub = ref(null);

// const normalSix = ref(null);
// const normalSeven = ref(null);
// const normalEight = ref(null);
// const normalTwentyOne = ref(null);
// const normalGitHub = ref(null);



const scrollToRef = (refName) => {

    
    //Add refs here
    const refs = {
        codeBlockRef,
        // codeBlockTwoRef,
        // codeBlockThreeRef,
        // codeBlockFourRef
    };

    const targetElement = refs[refName]?.value;

    if (targetElement) {
        targetElement.scrollIntoView({ behavior: 'smooth' });
    } else {
        console.warn("No target element found for refName:", refName);
    }
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

.gh-header {
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

.github-pic {
    width: 690px;
    height: 280px;
    margin-top: -5px;
}

.cmd-table {
    margin-top: -25px;
    width: 690px;
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

.bullet-pt {
    margin-top: -10px;
    margin-left: 20px;
    margin-bottom: 24px;
    font-size: 19px;
    width: 690px;
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

.bullet-pt-span {
    background-color: darkblue;
    border-radius: 50%;
    color: white;
    font-size: 15px;
    display: inline-block;
    width: 20px;
    height: 20px;
    text-align: center;
    line-height: 20px;
    margin-right: 6px;
}

@media (max-width: 700px) {
    .gh-header {
        width: 490px;
    }
    
    .description {
        width: 490px;
    }

    .github-pic {
        width: 490px;
        height: 200px;
    }
    
    .cmd-table {
        width: 490px;
    }

    .gh-header-two {
        width: 490px;
    }

    .description-two {
        width: 490px;
    }

    .bullet-pt {
        width: 490px;
    }
}
</style>
