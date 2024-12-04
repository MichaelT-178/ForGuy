<template>
    <div class="content-container">
        <h1 class="title">{{ text.page }}</h1>
        <p class="description">{{ text.desc }} <span @click="scrollToPracticeTable" class="scroll-txt">{{ text.desc2 }}</span> {{ text.desc3 }}</p>
        <CmdTable :tableName="createName"      :items="createCommands"      class="cmd-table"></CmdTable>
        <CmdTable :tableName="navigationName"  :items="navigationCommands"  class="cmd-table"></CmdTable>
        <CmdTable :tableName="displayName"     :items="displayCommands"     class="cmd-table"></CmdTable>
        <CmdTable :tableName="deleteName"      :items="deleteCommands"      class="cmd-table"></CmdTable>
        <CmdTable :tableName="programmingName" :items="programmingCommands" class="cmd-table"></CmdTable>
        <CmdTable :tableName="practiceName"    :items="practiceCommands"    class="cmd-table" ref="practiceTable"></CmdTable>
    </div>
    <p style="margin-bottom: 50px;"></p>
</template>


<script setup>
import { ref, nextTick } from 'vue';
import CmdTable from "../../components/CommandTable.vue";
import AllData from "../../data/Other/TerminalCommands.json";

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];

const createCommands = jsonData.value["Creation"];
const createName = createCommands[0].tableName;

const navigationCommands = jsonData.value["Navigation"];
const navigationName = navigationCommands[0].tableName;

const displayCommands = jsonData.value["Display"];
const displayName = displayCommands[0].tableName;

const deleteCommands = jsonData.value["Delete"];
const deleteName = deleteCommands[0].tableName;

const programmingCommands = jsonData.value["Programming"];
const programmingName = programmingCommands[0].tableName;

const practiceCommands = jsonData.value["Practice"];
const practiceName = practiceCommands[0].tableName;

const practiceTable = ref(null);

const scrollToPracticeTable = async () => {
    await nextTick();
    if (practiceTable.value) {
        practiceTable.value.$el.scrollIntoView({ behavior: 'smooth' });
    }
};

</script>


<style scoped>

.content-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%; 
}

.title, .description {
    width: 80%; 
    text-align: left; 
}

.description {
    margin-top: -13px;
    margin-left: 5px;
    font-size: 18px;
    margin-bottom: 11px;
}

.scroll-txt {
    color: #007AFF;
    cursor: pointer;
}

.scroll-txt:hover {
    color: #0000D7;
    text-decoration: underline;
}

.cmd-table {
    margin-bottom: 25px;
}

</style>
