<template>
    <div class="contact-card">
      <h2>Contact Information</h2>
      <div v-if="contact.Name">Name: {{ contact.Name }}</div>
      <div v-if="contact.Company">Company: {{ contact.Company }}</div>
      <div v-if="contact.Role">Role: {{ contact.Role }}</div>
      <div v-if="contact.Email">Email: <a :href="`mailto:${contact.Email}`">{{ contact.Email }}</a></div>
      <div v-if="contact.LinkedIn">LinkedIn: <a :href="contact.LinkedIn" target="_blank">{{ contact.LinkedIn }}</a></div>
      <p v-if="contact.Details">{{ contact.Details }}</p>
    </div>
  </template>
  
  <script setup>
  
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
      })
    }
  });
  </script>
  
  <style scoped>
  .contact-card {
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    max-width: 400px;
    margin: 20px auto;
  }
  </style>
  