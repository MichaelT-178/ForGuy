<template>
    <div class="image-container">
        <img src="../../assets/linkedIn.png" alt="LinkedIn Pic" />
        <div class="overlay"></div>
    </div>
    <div class="info-container">
        <h1>What is LinkedIn?</h1>
        <p>
            To keep it simple, LinkedIn is like Instagram for jobs. It's a place where you can apply to jobs, follow companies, 
            and create job alerts. There's also a social side to LinkedIn. You can follow your friends to see their job updates and 
            you can create a profile of your own. Job recruiters will typically view your profile to see if you're a good candidate 
            for a job, so try to make it nice and professional. You can also can also "connect" with other people and interact to 
            with their posts, make comments, etc. I would definitely consider LinkedIn an important part of your job search and 
            something worth checking out.
        </p>
    </div>
</template>

<style scoped>

.image-container {
    position: relative;
    width: 100%;
    height: 400px;
}

.info-container {
    margin-top: -5px;
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

h1 {
    margin-left: 100px;
}

p {
    margin-left: 101px;
    font-size: 20px;
    margin-top: -14px;
    width: 80%;
}

@media (max-width: 700px) {

    img, .overlay {
        height: 70%
    }

    .info-container {
        margin-top: -120px;
    }


    h1 {
        margin-left: 25px;
    }
    
    p {
        margin-left: 26px;
        width: 90%;
    }
}

</style>
