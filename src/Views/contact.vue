<template>
    <div class="contact-form">
      <h1>Contact Me</h1>
      <p class="intro-text">Feel free to message me and I'll try to reply as soon as possible!</p>
  
      <div class="form-group">
        <label for="name" class="form-label">Your Name*</label>
        <input type="text" id="name" name="name" v-model="userName" placeholder="Enter your name" />
      </div>
  
      <div class="form-group">
        <label for="email" class="form-label">Your Email*</label>
        <input type="email" id="email" name="email" v-model="userEmail" placeholder="Enter your email" />
      </div>
  
      <div class="form-group">
        <label for="message" class="form-label">Message*</label>
        <textarea id="message" name="message" v-model="userMessage" class="square-text-area" placeholder="Enter your message"></textarea>
      </div>

      <button 
  type="submit" 
  class="send-email-btn" 
  @click="submitForm" 
  :disabled="!isFormValid"
  :class="{
    'valid': isFormValid && !isButtonClicked,
    'clicked': isButtonClicked,
    'default': !isFormValid && !isButtonClicked
  }"
> 
Submit
</button>


    </div>
  </template>
  
  
  <script setup>
  import { ref, computed } from 'vue';
  
  const userName = ref('');
  const userEmail = ref('');
  const userMessage = ref('');

  const isButtonClicked = ref(false);

const submitForm = () => {
  isButtonClicked.value = true; // Update the click state
  console.log({ userName: userName.value, userEmail: userEmail.value, userMessage: userMessage.value });
  // Reset the click state after a delay if needed
  setTimeout(() => isButtonClicked.value = false, 500); // Optional: Reset after 2 seconds
};


  // Computed property to disable/enable the submit button
  const isFormValid = computed(() => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic regex for email validation
    return userName.value.trim() !== '' &&
           userEmail.value.match(emailRegex) &&
           userMessage.value.trim() !== '';
  });
  </script>
  

  <style scoped>
  .contact-form {
    display: flex;
    flex-direction: column;
    max-width: 600px;
    width: 90%;
    margin: 0 auto;
    padding: 20px;
  }
  
  .form-group {
    margin-bottom: 1rem;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-top: 9px; 
  }
  
  input[type="text"],
  input[type="email"],
  .square-text-area {
    width: 100%;
    border: 1.75px solid #ccc;
    padding: 12px;
    margin-top: 8px;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
  }
  
  input[type="text"]::placeholder,
  input[type="email"]::placeholder,
  .square-text-area::placeholder {
    font: arial;
    font-size: 14.25px;
    color: #999;
  }
  
  .square-text-area {
    height: 200px;
    resize: none;
  }
  
  .send-email-btn {
    width: 100%;
    color: white;
    cursor: pointer;
    border: none;
    padding: 10px;
    margin-top: 5px;
  }
  
  /* Default state when form is not valid */
  .send-email-btn.default {
    background-color: purple; /* Default color when form is invalid or not interacted */
  }
  
  /* State when form is valid but not clicked */
  .send-email-btn.valid {
    background-color: blue; /* Initial color when form is valid */
  }
  
  .send-email-btn.valid:hover {
    background-color: red; /* Hover color when form is valid */
  }
  
  /* State when button is clicked */
  .send-email-btn.clicked {
    background-color: green;
  }
  
  h1 {
    align-self: flex-start;
    margin-top: 5px;
  }
  
  .intro-text {
    margin-top: -15px;
    margin-bottom: 16px;
  }
  </style>
  
  
