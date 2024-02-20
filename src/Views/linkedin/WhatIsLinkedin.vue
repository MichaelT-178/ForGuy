<template>
    <div class="image-container">
        <img src="../../assets/linkedIn.png" alt="LinkedIn Pic" />
        <div class="overlay"></div>
    </div>
    <h1>What is LinkedIn?</h1>
    <p>This is the What is LinkedIn page</p>
</template>

<style scoped>

.image-container {
    position: relative;
    width: 100%;
    height: 400px;
}

img {
    width: 100%; 
    height: 100%;
    display: block;
}

.overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(8, 0, 255, 0.059);
}

</style>
