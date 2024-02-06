<template>
    <main class="about-page">
        <h1>Resume Template</h1>
        <p>This is the Resume Template page</p>
        <button @click="downloadResumeDocx">Download DOCX</button>
    </main>
</template>

<script setup>

function downloadResumeDocx(){
  const docxUrl = 'https://michaelt-178.github.io/TestWebsite/ResumeTemplate.docx';
  const link = document.createElement('a');

  link.href = docxUrl;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};

</script>


