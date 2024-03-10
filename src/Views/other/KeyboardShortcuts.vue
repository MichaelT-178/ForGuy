<template>
    <main class="about-page">
        <h1>Keyboard Shortcuts</h1>
        <p>This is the Keyboard Shortcuts page</p>
        <ShortcutTable :shortcuts="shortcuts"></ShortcutTable>
    </main>
</template>


<script setup>
import { ref } from 'vue';
import ShortcutTable from "../../components/ShortcutTable.vue";
import AllData from "../../data/Other/KeyboardShortcuts.json";

const jsonData = ref(AllData);
const shortcuts = jsonData.value["Shortcuts"];

console.log(shortcuts)

</script>