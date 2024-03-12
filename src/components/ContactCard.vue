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
  padding: 0px 0px 10px 30px; /* Top, right, bottom, left */
  border: 1px solid #ccc;
  border-radius: 8px;
  width: 600px;
  margin: 20px auto;
  position: relative; /* Add this line */
  overflow: hidden; /* Add this to ensure the image does not overflow the card */
}

.contact-card img {
  position: absolute; /* Position the image absolutely within the contact-card */
  top: 35px; /* Adjust this to create space between the top of the card and the image */
  right: 30px; /* Adjust this to create space between the right side of the card and the image */
  width: 100px; /* Adjust the width as needed to make the image smaller */
  height: 100px;
  height: auto; /* Maintain the aspect ratio */
  border: 1px solid #999999; /* Add a border with 2px width and a color of #ccc */
}


@media (max-width: 700px) {
  .contact-card {
    width: 425px;
  }
  
  .contact-card img {
    width: 85px; /* Optionally, make the image even smaller on smaller screens */
    height: 85px; /* Optionally, make the image even smaller on smaller screens */
  }
}
</style>

