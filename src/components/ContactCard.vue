<template>
  <div class="contact-card">
    <h2><span>Contact Information</span></h2>
    <div v-if="contact.Name"><span class="attr">Name</span>: {{ contact.Name }}</div>
    <div v-if="contact.Company"><span class="attr">Company</span>: {{ contact.Company }}</div>
    <div v-if="contact.Role"><span class="attr">Role</span>: {{ contact.Role }}</div>
    <div v-if="contact.Email"><span class="attr">Email</span>: <a :href="`mailto:${contact.Email}`" class="blue-link">{{ contact.Email }}</a></div>
    <div v-if="contact.Contact"><span class="attr">Contact</span>: <a :href="contact.Contact" target="_blank" class="blue-link">{{ contact.Contact }}</a></div>
    <template v-if="contact.LinkedIn">
      <span class="attr">LinkedIn</span>:
      <template v-if="contact.LinkedIn.includes('https')">
        <a :href="contact.LinkedIn" target="_blank" class="purple-link">{{ contact.LinkedIn }}</a>
      </template>
      <template v-else>
        <router-link to="/ContactMe" class="blue-link">{{ contact.LinkedIn }}</router-link>
      </template>
    </template>
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

.contact-card h2 span {
  border-bottom: 1px solid #ccc;
  padding-bottom: 1px;
  display: inline-block;
  padding-right: 110px;
}

.contact-card h2 {
  margin-bottom: 20px;
}

.contact-card div {
  margin-bottom: 7px;
}

.attr {
  font-weight: 560;
}

.contact-card p {
  padding: 0px 15px 0px 0px;
}

.contact-card {
  padding: 0px 0px 10px 30px; /* Top, right, bottom, left */
  border: 1px solid #ccc;
  border-radius: 8px;
  width: 600px;
  margin: 20px auto;
  position: relative;
  overflow: hidden;
  background: white;
  border-top: 2px solid darkblue; 
  border-bottom: 2px solid darkblue; 
}

.blue-link {
  color: #0000EE; 
}

.blue-link:hover {
  color: #000086;
}

.purple-link:hover {
  color: #2E0057;
}

.contact-card img {
  position: absolute;
  top: 40px;
  right: 37px;
  width: 100px;
  height: 100px; 
  border: 1px solid #999999;
}

@media (max-width: 700px) {
  .contact-card {
    width: 425px;
  }
  
  .contact-card img {
    width: 85px;
    height: 85px;
  }

  .contact-card h2 span {
    padding-right: 48px;
  }
}

</style>

