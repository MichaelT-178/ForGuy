<template>
    <div class="content-container">
        <h1 class="title">Terminal Commands</h1>
        <p class="description">This is the Terminal Commands page</p>
        <CmdTable tableName="Create"      :items="createCommands"      class="cmd-table"></CmdTable>
        <CmdTable tableName="Navigation"  :items="navigationCommands"  class="cmd-table"></CmdTable>
        <CmdTable tableName="Display"     :items="displayCommands"     class="cmd-table"></CmdTable>
        <CmdTable tableName="Delete"      :items="deleteCommands"      class="cmd-table"></CmdTable>
        <CmdTable tableName="Programming" :items="programmingCommands" class="cmd-table"></CmdTable>
    </div>
    <p style="margin-bottom: 50px;"></p>
</template>


<script setup>
import { ref } from 'vue';
import CmdTable from "../../components/CommandTable.vue";
import AllData from "../../data/Other/TerminalCommands.json";

const jsonData = ref(AllData);
const createCommands = jsonData.value["Creation"];
const navigationCommands = jsonData.value["Navigation"];
const displayCommands = jsonData.value["Display"];
const deleteCommands = jsonData.value["Delete"];
const programmingCommands = jsonData.value["Programming"];

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

.cmd-table {
    margin-bottom: 25px;
}

</style>