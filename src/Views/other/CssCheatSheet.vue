<template>
  <div class="content-container">
      <h1 class="title">{{ text.page }}</h1>
      <p class="description">{{ text.desc }}</p>
      <CmdTable :tableName="colorName"       :items="colorProperties"       class="cmd-table"></CmdTable>
      <CmdTable :tableName="navigationName"  :items="navigationProperties"  class="cmd-table"></CmdTable>
      <CmdTable :tableName="displayName"     :items="displayProperties"     class="cmd-table"></CmdTable>
      <CmdTable :tableName="deleteName"      :items="deleteProperties"      class="cmd-table"></CmdTable>
      <CmdTable :tableName="programmingName" :items="programmingProperties" class="cmd-table"></CmdTable>
      <CmdTable :tableName="practiceName"    :items="practiceProperties"    class="cmd-table" ref="practiceTable"></CmdTable>
  </div>
  <p style="margin-bottom: 50px;"></p>
</template>


<script setup>
import { ref, nextTick } from 'vue';
import CmdTable from "../../components/CommandTable.vue";
import AllData from "../../data/Other/CSSCheatSheet.json";

const jsonData = ref(AllData);
const text = jsonData.value["Text"][0];

const colorProperties = jsonData.value["Colors"];
const colorName = colorProperties[0].tableName;

const navigationProperties = jsonData.value["Navigation"];
const navigationName = navigationProperties[0].tableName;

const displayProperties = jsonData.value["Display"];
const displayName = displayProperties[0].tableName;

const deleteProperties = jsonData.value["Delete"];
const deleteName = deleteProperties[0].tableName;

const programmingProperties = jsonData.value["Programming"];
const programmingName = programmingProperties[0].tableName;

const practiceProperties = jsonData.value["Practice"];
const practiceName = practiceProperties[0].tableName;




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
