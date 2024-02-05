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
            { text: "Offers I've Recieved",  icon: "handshake",    link: "/jobs/OffersRecieved" },
            { text: "Interview Tips",        icon: "group",        link: "/jobs/InterviewTips" },
            { text: "Helpful Websites",      icon: "wysiwyg",      link: "/jobs/HelpfulWebsites" },
            { text: "Job Tips",              icon: "lightbulb",    link: "/jobs/JobTips.vue" }
        ],
    },
    {
        text: "LinkedIn",
        subMenu: [
            { text: "What Is LinkedIn?",  icon: "person_add",      link: "/linkedin/WhatIsLinkedin" },
            { text: "Setup a Profile",    icon: "account_circle",  link: "/linkedin/SetupProfile" },
            { text: "Setup Job Alerts",   icon: "notifications",   link: "/linkedin/SetupJobAlerts" },
            { text: "LinkedIn Tips",      icon: "psychology",      link: "/linkedin/LinkedinTips" }
        ],
    },
    {
        text: "Classes",
        subMenu: [
            { text: "Class Recommendations",  icon: "thumb_up",     link: "/classes/ClassRecommendations" },
            { text: "CSC Descriptions",       icon: "description",  link: "/classes/CSCDescriptions" },
            { text: "Classes I've Taken",     icon: "co_present",   link: "/classes/ClassesIveTaken" }, //interactive_space
            { text: "Classes To Avoid",       icon: "cancel",       link: "/classes/ClassesToAvoid" }
        ],
    },
    {
        text: "Comp Sci",
        subMenu: [
            { text: "Visual Studio Code",  icon: "laptop_mac",         link: "/CompSci/VisualStudioCode" },
            { text: "VSCode Settings",     icon: "settings",           link: "/CompSci/VSCodeSettings" },
            { text: "VSCode Shorcuts",     icon: "forward_media",      link: "/CompSci/VSCodeShortcuts" },
            { text: "Extensions",          icon: "extension",          link: "/CompSci/VSCodeShortcuts" },
            { text: "Favorite Libraries",  icon: "library_add_check",  link: "/CompSci/FavoriteLibraries" },
            { text: "Comp Sci Tips",       icon: "device_hub",         link: "/CompSci/CompSciTips" } 
        ],
    },
    {
        text: "Other",
        subMenu: [
            { text: "General Tips",       icon: "self_improvement",  link: "/other/GeneralTips" },
            { text: "Apps To Download",   icon: "phone_iphone",      link: "/other/AppsToDownload" },
            { text: "CS Stuff I Like",    icon: "favorite",          link: "/other/CompSciStuff" },
            { text: "Terminal Commands",  icon: "terminal",          link: "/other/TerminalCommands" },
            { text: "Memes",              icon: "comedy_mask",       link: "/other/Memes" }
        ],
    },
    {
        text: "Contact",
        route: '/ContactMe'
    },
];

</script>