<template>
    <ShortcutTable 
        :title="title" 
        :description="description" 
        :shortcuts="shortcuts">
    </ShortcutTable>
    <p style="margin-bottom: 100px;"></p>
</template>


<script setup>
import { ref } from 'vue';
import AllData from '../../data/Other/KeyboardShortcuts.json';
import ShortcutTable from '../../components/ShortcutTable.vue';

const jsonData = ref(AllData);
const title = jsonData.value["Title"];
const description = jsonData.value["Description"];
const shortcuts = jsonData.value["Shortcuts"];

</script>