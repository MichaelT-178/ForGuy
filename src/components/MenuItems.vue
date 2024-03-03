<script>

export const menuItems = [
    {
        text: "Home",
        route: "/",
    },
    {
        text: "Jobs",
        subMenu: [
            { text: "Where To Apply",        icon: "work",         link: "/jobs/WhereToApply" },
            { text: "Resume Template",       icon: "description",  link: "/jobs/ResumeTemplate" },
            { text: "How To Get a Job",      icon: "lightbulb",    link: "/jobs/HowToGetAJob.vue" },
            { text: "Offers I've Recieved",  icon: "handshake",    link: "/jobs/OffersRecieved" },
            { text: "Interview Tips",        icon: "group",        link: "/jobs/InterviewTips" },
            { text: "Career Path Advice",    icon: "explore",      link: "/jobs/CareerPathAdvice" }
        ]
    },
    {
        text: "LinkedIn",
        subMenu: [
            { text: "What Is LinkedIn?",  icon: "person_add",      link: "/linkedin/WhatIsLinkedin" },
            { text: "Setup a Profile",    icon: "account_circle",  link: "/linkedin/SetupProfile" },
            { text: "Setup Job Alerts",   icon: "notifications",   link: "/linkedin/SetupJobAlerts" },
            { text: "LinkedIn Tips",      icon: "psychology",      link: "/linkedin/LinkedinTips" },
            { text: "Contacts",           icon: "person",          link: "/linkedin/Contacts" }
        ]
    },
    {
        text: "Classes",
        subMenu: [
            { text: "Class Recommendations",  icon: "thumb_up",       link: "/classes/ClassRecommendations" },
            { text: "CSC Descriptions",       icon: "description",    link: "/classes/CSCDescriptions" },
            { text: "Classes I've Taken",     icon: "co_present",     link: "/classes/ClassesIveTaken" }, //interactive_space
            { text: "Classes To Avoid",       icon: "cancel",         link: "/classes/ClassesToAvoid" },
            { text: "Useful Certifications",  icon: "editor_choice",  link: "/classes/Certifications" }
        ]
    },
    {
        text: "Comp Sci",
        subMenu: [
            { text: "Visual Studio Code",  icon: "laptop_mac",         link: "/CompSci/VisualStudioCode" },
            { text: "What is GitHub?",     icon: "hub",                link: "/CompSci/GitHub" },
            { text: "VSCode Settings",     icon: "settings",           link: "/CompSci/VSCodeSettings" },
            { text: "UI/UX Design Tips",   icon: "brush",              link: "/CompSci/UIDesignTips" },
            { text: "VSCode Extensions",   icon: "extension",          link: "/CompSci/VSCodeExtensions" },
            { text: "VSCode Shortcuts",    icon: "rocket_launch",      link: "/CompSci/VSCodeShortcuts" },
            { text: "Comp Sci Tips",       icon: "device_hub",         link: "/CompSci/CompSciTips" } 
        ]
    },
    {
        text: "Other",
        subMenu: [
            { text: "General Tips",        icon: "self_improvement",  link: "/other/GeneralTips" },
            { text: "Apps To Download",    icon: "phone_iphone",      link: "/other/AppsToDownload" },
            { text: "CS Stuff I Like",     icon: "favorite",          link: "/other/CompSciStuff" },
            { text: "Terminal Commands",   icon: "terminal",          link: "/other/TerminalCommands" },
            { text: "Keyboard Shortcuts",  icon: "bolt",              link: "/other/KeyboardShortcuts" },
            { text: "Memes",               icon: "comedy_mask",       link: "/other/Memes" },
            { text: "UNCW Pictures",       icon: "photo_camera",      link: "/other/UncwPics" }
        ]
    },
    {
        text: "Contact",
        route: "/ContactMe"
    }
];

</script>