<template>
    <div class="center-container">
        <div class="header-container">
            <h1>Keyboard Shortcuts</h1>
            <p>This is the Keyboard Shortcuts page</p>
        </div>
        <div class="shortcut-table-container">
            <ShortcutTable :shortcuts="shortcuts"></ShortcutTable>
        </div>
    </div>
</template>


<script setup>
import { ref } from 'vue';
import ShortcutTable from "../../components/ShortcutTable.vue";
import AllData from "../../data/Other/KeyboardShortcuts.json";

const jsonData = ref(AllData);
const shortcuts = jsonData.value["Shortcuts"];

</script>


<style scoped>

.center-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 80%;
    margin: auto;
}

.header-container {
    align-self: flex-start;
    width: 100%;
    padding-left: 15.5%;
}

.shortcut-table-container {
    width: 100%;
    display: flex;
    justify-content: center;
    margin-bottom: 100px;
}

p {
    margin-top: -13px;
    margin-bottom: 17px;
}

@media (max-width: 700px) {
    .shortcut-table-container {
        width: 150%
    }

    .header-container {
        align-self: flex-start;
        width: 100%;
        padding-left: 0.25%;
    }
}

</style>