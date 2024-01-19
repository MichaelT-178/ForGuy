<script>

export const menuItems = [
    {
        text: "Home",
        route: "/about",
    },
    {
        text: "Jobs",
        subMenu: [
            { text: "Where To Apply", link: "/apply" },
            { text: "Resume Template", link: "/about" },
            { text: "Offers I've Recieved", link: "/about" },
            { text: "Interview Tips", link: "/about" },
            { text: "Helpful Website", link: "/about" },
            { text: "Job Tips", link: "/about" },
        ],
    },
    {
        text: "LinkedIn",
        subMenu: [
            { text: "What Is LinkedIn?", link: "/subitem-2-1" },
            { text: "Setup a Profile", link: "/subitem-2-2" },
            { text: "Setup Job Alerts", link: "/subitem-2-3" },
            { text: "LinkedIn Tips", link: "/subitem-2-4" },
        ],
    },
    {
        text: "Classes",
        subMenu: [
            { text: "Class Recommendations", link: "/subitem-2-1" },
            { text: "CSC Descriptions", link: "/subitem-2-2" },
            { text: "Classes I've Taken", link: "/subitem-2-3" },
            { text: "Classes To Avoid", link: "/subitem-2-4" },
        ],
    },
    {
        text: "Comp Sci",
        subMenu: [
            { text: "Visual Studio Code", link: "/subitem-2-1" },
            { text: "VSCode Settings", link: "/subitem-2-2" },
            { text: "VSCode Shorcuts", link: "/subitem-2-3" },
            { text: "Favorite Libraries", link: "/subitem-2-4" },
            { text: "Comp Sci Tips", link: "/subitem-2-5" },
        ],
    },
    {
        text: "Other",
        subMenu: [
            { text: "General Tips", link: "/subitem-2-1" },
            { text: "Apps To Download", link: "/subitem-2-2" },
            { text: "CS Stuff I Like", link: "/subitem-2-3" },
            { text: "Terminal Commands", link: "/subitem-2-4" },
            { text: "Memes", link: "/subitem-2-5" },
        ],
    },
    {
        text: "Contact Me",
        route: "/"
    },
];

</script>