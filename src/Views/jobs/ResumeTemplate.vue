<template>
    <main class="about-page">
        <h1>Resume Template</h1>
        <p>This is the Resume Template page</p>
        <button @click="downloadDocx">Download DOCX</button>
        <a download="COOL.docx" href="/Users/michaeltotaro/top-bar/src/data/jobs/ElijahResume.docx">YEET</a>
    </main>
</template>

<script setup>
import { ref } from 'vue';

const downloadDocx = () => {
    fetch("../../data/jobs/ElijahResume.docx")
        .then(response => {
            console.log(response)
            console.log(response.url);
        });
        //.then(response => response.blob())
        // .then(blob => {
        //     const url = window.URL.createObjectURL(blob);
        //     const a = document.createElement('a');
        //     a.href = url;
        //     a.download = 'filename.docx'; // Specify the file name
        //     document.body.appendChild(a); // Required for this to work in FireFox
        //     a.click();
        //     a.remove(); // Cleanup
        // })
        // .catch(err => console.error('Download error:', err));
}

</script>