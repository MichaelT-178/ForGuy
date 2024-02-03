<script>

export const menuItems = [
    {
        text: "Home",
        route: "/about",
    },
    {
        text: "Jobs",
        subMenu: [
            { text: "Where To Apply", link: "/jobs/WhereToApply" },
            { text: "Resume Template", link: "/jobs/ResumeTemplate" },
            { text: "Offers I've Recieved", link: "/jobs/OffersRecieved" },
            { text: "Interview Tips", link: "/jobs/InterviewTips" },
            { text: "Helpful Websites", link: "/jobs/HelpfulWebsites" },
            { text: "Job Tips", link: "/jobs/JobTips.vue" },
        ],
    },
    {
        text: "LinkedIn",
        subMenu: [
            { text: "What Is LinkedIn?", link: "/linkedin/WhatIsLinkedin" },
            { text: "Setup a Profile", link: "/linkedin/SetupProfile" },
            { text: "Setup Job Alerts", link: "/linkedin/SetupJobAlerts" },
            { text: "LinkedIn Tips", link: "/linkedin/LinkedinTips" },
        ],
    },
    {
        text: "Classes",
        subMenu: [
            { text: "Class Recommendations", link: "/classes/ClassRecommendations" },
            { text: "CSC Descriptions", link: "/classes/CSCDescriptions" },
            { text: "Classes I've Taken", link: "/classes/ClassesIveTaken" },
            { text: "Classes To Avoid", link: "/classes/ClassesToAvoid" },
        ],
    },
    {
        text: "Comp Sci",
        subMenu: [
            { text: "Visual Studio Code", link: "/CompSci/VisualStudioCode" },
            { text: "VSCode Settings", link: "/CompSci/VSCodeSettings" },
            { text: "VSCode Shorcuts", link: "/CompSci/VSCodeShortcuts" },
            { text: "Favorite Libraries", link: '/CompSci/FavoriteLibraries' },
            { text: "Comp Sci Tips", link: "/CompSci/CompSciTips" },
        ],
    },
    {
        text: "Other",
        subMenu: [
            { text: "General Tips", link: "/other/GeneralTips" },
            { text: "Apps To Download", link: "/other/AppsToDownload" },
            { text: "CS Stuff I Like", link: "/other/CompSciStuff" },
            { text: "Terminal Commands", link: "/other/TerminalCommands" },
            { text: "Memes", link: "/other/Memes" },
        ],
    },
    {
        text: "Contact",
        route: '/ContactMe'
    },
];

</script>