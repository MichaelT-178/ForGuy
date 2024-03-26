<template>
    <div class="container">
        <h1 class="contact-header">Contacts</h1>
        <p class="description">These are useful job contacts from various companies.</p>
        <div class="contacts-container">
            <div v-for="contact in contacts" :key="contact.Company" class="contact-section">
                <ContactCard :contact="contact"></ContactCard>
            </div>
        </div>
        <p style="margin-bottom: 60px;"></p>
    </div>
</template>


<script setup>
import { ref } from 'vue';
import AllData from "../../data/LinkedIn/Contacts.json";
import ContactCard from "../../components/ContactCard.vue"

const jsonData = ref(AllData);
const contacts = jsonData.value["Contacts"];

</script>


<style scoped>

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.contact-header {
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

.contacts-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.contact-section {
    margin-top: -19px;
}

@media (max-width: 700px) {
    .contact-header {
        width: 490px;
    }
    
    .description {
        width: 490px;
    }

    .contact-section {
        width: 400px;
        margin-right: 70px;
    }
}

</style>
