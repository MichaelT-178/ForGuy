<template>
  <div class="contact-card">
    <h2>Contact Information</h2>
    <div v-if="contact.Name">Name: {{ contact.Name }}</div>
    <div v-if="contact.Company">Company: {{ contact.Company }}</div>
    <div v-if="contact.Role">Role: {{ contact.Role }}</div>
    <div v-if="contact.Email">Email: <a :href="`mailto:${contact.Email}`">{{ contact.Email }}</a></div>
    <div v-if="contact.LinkedIn">LinkedIn: <a :href="contact.LinkedIn" target="_blank">{{ contact.LinkedIn }}</a></div>
    <p v-if="contact.Details">{{ contact.Details }}</p>
    <img :src="imagePath" alt="Company Image">
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  contact: {
    type: Object,
    default: () => ({
      Name: "",
      Company: "",
      Role: "",
      Email: "",
      LinkedIn: "",
      Details: "",
      Image: ""
    })
  }
});

const imagePath = ref(new URL(`../assets/Companies/${props.contact.Image}`, import.meta.url).href);

</script>

<style scoped>
.contact-card {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  width: 600px;
  margin: 20px auto;
}

@media (max-width: 700px) {
  .contact-card {
    width: 425px;
  }
}
</style>
