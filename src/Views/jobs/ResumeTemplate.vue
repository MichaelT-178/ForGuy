<template>
    <main class="about-page">
        <h1>Resume Template</h1>
        <p>This is the Resume Template page</p>
        <button @click="downloadResumeDocx">Download DOCX</button>
    </main>
</template>

<script setup>

function downloadResumeDocx() {

  //Can't use local file because of security reasons.
  const docxUrl = 'https://michaelt-178.github.io/TestWebsite/Practice.docx';
  //http://localhost:5173/src/data/jobs/ResumeTemplate.docx

  const link = document.createElement('a');

  link.href = docxUrl;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

</script>


