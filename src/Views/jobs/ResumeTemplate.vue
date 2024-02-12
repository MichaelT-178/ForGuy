<template>
  <main class="about-page">
      <h1>Resume Template</h1>
      <p>This is the Resume Template page</p>
      <button @click="downloadResumeDocx">Download DOCX</button>
      <span>{{ currentPage }}/{{ totalPageCount }}</span>
      <div class="pdf-page-container" @scroll="updateCurrentPage">
          <img v-for="(pageUrl, index) in pdfPageUrls" :src="pageUrl" :key="`page-${index}`" alt="PDF Page" class="pdf-page-image"/>
      </div>
  </main>
</template>



<script setup>
import { ref } from 'vue';
import ResumePic1 from "../../data/jobs/ElijahResume/ElijahResume1.png";
import ResumePic2 from "../../data/jobs/ElijahResume/ElijahResume2.png";

const pdfPageUrls = ref([ResumePic1, ResumePic2]);
const currentPage = ref(1);
const totalPageCount = pdfPageUrls.value.length;

function downloadResumeDocx() {
  const docxUrl = 'https://michaelt-178.github.io/TestWebsite/Practice.docx';
  const link = document.createElement('a');
  link.href = docxUrl;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

function updateCurrentPage(event) {
  const container = event.target;
  const scrollPosition = container.scrollTop + container.offsetHeight;
  const pageHeight = container.scrollHeight / totalPageCount;
  currentPage.value = Math.min(totalPageCount, Math.round(scrollPosition / pageHeight));
}
</script>



<style scoped>
.pdf-page-container {
  max-height: 900px; /* Adjust based on your needs */
  overflow-y: auto; /* Enables vertical scrolling */
  border: 2px solid #000000;
  width: 700px; /* Adjust width as needed */
  margin-top: 20px;
  margin-bottom: 200px;
  
}

.pdf-page-image {
  width: 100%; /* Images fill the container width */
  display: block; /* Ensures images are laid out without extra space */
  border-bottom: 1px solid black; /* Adds a thin black line between images */
}
</style>
