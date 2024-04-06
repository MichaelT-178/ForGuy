<template>
    <div class="container">
        <h1 class="gh-header">GitHub</h1>
        <p class="description">This is a description of GitHub and common commands.</p>
        <img src="../../assets/GitHub.png" alt="GitHub" class="github-pic"/>
        
        <h2 class="gh-header-two">What is GitHub and Git?</h2>
        <p class="description-two">How to get an existing folder onto GitHub.</p>\

        <!-- How to create a GitHub account Section -->
        <h2 class="gh-header-two">How to Create a GitHub Account</h2>
        <p class="description-two">These are instructions to setup Git and create a GitHub account.</p>

        <div v-for="point in setupGitHub" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>

        
        <!-- How to create a GitHub Repository Section -->
        <h2 class="gh-header-two">How to Create a GitHub Repository</h2>
        <p class="description-two">This is how you create a GitHub repo and set it up locally.</p>

        <div v-for="point in createGitHubRepo" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>


        <!-- How to create a Second GitHub account Section -->
        <h2 class="gh-header-two">How to Create Another GitHub Account</h2>
        <p class="description-two">To add another GitHub account to your computer do the original 5-25 steps with these modified steps.</p>

        <div v-for="point in setupSecondGitHub" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>


        <!-- How to create a Second GitHub Repository Section -->
        <h2 class="gh-header-two">How to Create a GitHub Repository Using a Different Account</h2>
        <p class="description-two">This is how you create a GitHub repository for an account other than your main one</p>

        <div v-for="point in createSecondGitHubRepo" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}
                </span><span v-html="createHyperLink(processedTipContent(point.instruction))" v-bind="point.ref ? { ref : point.ref } : {}"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>
        

        <!-- General Tips for Working with GitHub -->
        <h2 class="gh-header-two" ref="codeBlockRef">General Tips</h2>
        <p class="description-two">These are general tips for working with GitHub</p>

        <div v-for="tip in generalTips" :key="tip.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ tip.id }}</span><span v-html="createHyperLink(tip.instruction)"></span></p>
            <span v-if="tip.Code"><CodeBlock :codeInfo="tip.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>



        <!-- Upload Existing Folder section -->
        <h2 class="gh-header-two" ref="codeBlockRef">How to Fork a Repository</h2>
        <p class="description-two">How to create a fork of a repository on GitHub. A fork is copying another persons repository onto your account, so you can modify it without changing theirs.</p>

        <div v-for="point in createFork" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
            <span v-if="point.Code"><CodeBlock :codeInfo="point.Code" style="margin-bottom: 20px;"></CodeBlock></span>
        </div>


        <!-- Upload Existing Folder section -->
        <h2 class="gh-header-two" ref="codeBlockRef">Existing Folder Commands</h2>
        <p class="description-two">How to get an existing folder onto GitHub.</p>

        <div v-for="point in existingFolderPts" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <CmdTable tableName="" :items="existingFolderCmds" class="cmd-table" ref="practiceTable"></CmdTable>

        

        <!-- Amotions Workflow -->
        <h2 class="gh-header-two" ref="codeBlockRef">Amotions Workflow</h2>
        <p class="description-two">This was my git workflow at Amotions. It's a little more extensive than your average workflow since we pushed to production so fast.</p>


        <CmdTable tableName="" :items="amotionsWorkflowOne" class="cmd-table" ref="practiceTable"></CmdTable>

        <p class="centered-txt">* Make changes/additions to code. Close terminal *</p>

        <CmdTable tableName="" :items="amotionsWorkflowTwo" class="cmd-table" ref="practiceTable"></CmdTable>

        <p class="centered-txt">Make a pull request on github.</p>

        <div v-for="point in amotionsPts" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <p class="centered-txt">Once branch is merged into dev. Merge into Main.</p>

        <div v-for="point in amotionsPtsTwo" :key="point.id">
            <p class="bullet-pt"><span class="bullet-pt-span">{{ point.id }}</span><span v-html="createHyperLink(point.instruction)"></span></p>
        </div>

        <p class="centered-txt">Git Deletion Commands</p>

        <CmdTable tableName="" :items="amotionsWorkflowThree" class="cmd-table" ref="practiceTable"></CmdTable>
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
const createGitHubRepo = jsonData.value["CreateGitHubRepo"];



const setupSecondGitHub = jsonData.value["SetupSecondGitHub"];
const createSecondGitHubRepo = jsonData.value["CreateSecondGitHubRepo"];


const generalTips = jsonData.value["GeneralTips"];


const amotionsWorkflowOne = jsonData.value["AmotionsWorkflowOne"];
const amotionsWorkflowTwo = jsonData.value["AmotionsWorkflowTwo"];
const amotionsWorkflowThree = jsonData.value["AmotionsWorkflowThree"];

const amotionsPts = jsonData.value["AmotionsPts"];
const amotionsPtsTwo = jsonData.value["AmotionsPtsTwo"];



const createFork = jsonData.value["CreateFork"];






const existingFolderPts = jsonData.value["ExistingFolderPts"];
const existingFolderCmds = jsonData.value["ExistingFolder"];





//Add refs here
const codeBlockRef = ref(null);
// const codeBlockTwoRef = ref(null);
// const codeBlockThreeRef = ref(null);
// const codeBlockFourRef = ref(null);

const secondSix = ref(null);
const secondSeven = ref(null);
const secondNine = ref(null);
const secondTwentyThree = ref(null);
const secondGitHubSeven = ref(null);
const secondGitHubEight = ref(null);

const normalSix = ref(null);
const normalSeven = ref(null);
const normalNine = ref(null);
const normalTwentyThree = ref(null);
const normalGitHubSeven = ref(null);
const normalGitHubEight = ref(null);



const scrollToRef = (refName) => {

    const offset = 80;

    const refs = {
        secondSix,
        secondSeven,
        secondNine,
        secondTwentyThree,
        secondGitHubSeven,
        secondGitHubEight,
        normalSix,
        normalSeven,
        normalNine,
        normalTwentyThree,
        normalGitHubSeven,
        normalGitHubEight
    };

    const targetElement = refs[refName]?.value;

    if (targetElement) {
        const elementPosition = targetElement.getBoundingClientRect().top + window.scrollY;
        const offsetPosition = elementPosition - offset;

        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    } else {
        console.warn("No target element found for refName:", refName);
    }
}

const processedTipContent = (tip) => {
    return tip.replace(/(Different for multiple accounts|Scroll back up to original step)\((.*?)\)/g, (match, phrase, refName) => {
        return `<span href="#" class="scroll-down" data-ref-name="${refName}">${phrase}</span>`;
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

.centered-txt {
    text-align: center; 
    font-size: 23.5px; 
    margin-top: 25px;
    margin-bottom: 25px;
    margin-right: 40px;
    cursor: pointer;
    color: black;
    font-weight: bold;
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
    display: flex;
    align-items: flex-start;
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
