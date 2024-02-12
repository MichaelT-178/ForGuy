<template>
  <div class="contact-form">
    <h1>Contact Me</h1>
    <p class="intro-text">Feel free to message me and I'll try to reply as soon as possible!</p>

    <div class="form-group">
      <label for="name" class="form-label">Your Name*</label>
      <input autocomplete="off" type="text" id="name" name="name" v-model="userName" placeholder="Enter your name"/>
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
  :class="{'valid': isFormValid && !isButtonClicked, 'clicked': isButtonClicked, 'default': !isFormValid && !isButtonClicked}">
  {{ buttonText }}
</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import emailjs from 'emailjs-com';
import Swal from 'sweetalert2';

const userName = ref('');
const userEmail = ref('');
const userMessage = ref('');
const isButtonClicked = ref(false);
const buttonText = ref('Submit'); // Button text management

// Initialize EmailJS with your user ID
emailjs.init('bCe2UFI1L7SfXITtA');

const isFormValid = computed(() => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return userName.value.trim() !== '' &&
         userEmail.value.match(emailRegex) &&
         userMessage.value.trim() !== '';
});

const submitForm = () => {
  if (!isFormValid.value) return;

  isButtonClicked.value = true;
  buttonText.value = 'Sending...'; // Change button text to "Sending..."

  const templateParams = {
    from_name: userName.value,
    from_email: userEmail.value,
    message: userMessage.value,
  };

  const serviceID = 'default_service';
  const templateID = 'template_ngfg5ko';

  emailjs.send(serviceID, templateID, templateParams)
    .then((response) => {
      Swal.fire('Success!', 'Your message has been sent successfully.', 'success');
      userName.value = '';
      userEmail.value = '';
      userMessage.value = '';
    }, (err) => {
      Swal.fire('Error!', 'Something went wrong with your message.', 'error');
      console.error('Failed to send email:', err);
    })
    .finally(() => {
      isButtonClicked.value = false;
      buttonText.value = 'Submit'; // Reset button text to "Submit"
    });
};
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
  
  
