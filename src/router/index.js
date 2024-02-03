import { createRouter, createWebHistory } from 'vue-router';

//Home 
import Home from '../views/Home.vue';

//Jobs 
import WhereToApply from '../views/jobs/WhereToApply.vue';
import ResumeTemplate from '../views/jobs/ResumeTemplate.vue';
import OffersRecieved from '../views/jobs/OffersRecieved.vue';
import InterviewTips from '../views/jobs/InterviewTips.vue';
import HelpfulWebsites from '../views/jobs/HelpfulWebsites.vue';
import JobTips from '../views/jobs/JobTips.vue'

//Linkedin 
import WhatIsLinkedin from '../views/linkedin/WhatIsLinkedin.vue';
import SetupProfile from '../views/linkedin/SetupProfile.vue';
import SetupJobAlerts from '../views/linkedin/SetupJobAlerts.vue';
import LinkedinTips from '../views/linkedin/LinkedinTips.vue';

//Classes 
import ClassRecommendations from '../views/classes/ClassRecommendations.vue';
import CSCDescriptions from '../views/classes/CSCDescriptions.vue';
import ClassesIveTaken from '../views/classes/ClassesIveTaken.vue';
import ClassesToAvoid from '../views/classes/ClassesToAvoid.vue';

//Comp Sci
import VisualStudioCode from '../views/compsci/VisualStudioCode.vue';
import VSCodeSettings from '../views/compsci/VSCodeSettings.vue';
import VSCodeShortcuts from '../views/compsci/VSCodeShortcuts.vue';
import FavoriteLibraries from '../views/compsci/FavoriteLibraries.vue';
import CompSciTips from '../views/compsci/CompSciTips.vue';

//Other 
import GeneralTips from '../views/other/GeneralTips.vue';
import AppsToDownload from '../views/other/AppsToDownload.vue';
import CsStuffILike from '../views/other/CsStuffILike.vue';
import TerminalCommands from '../views/other/TerminalCommands.vue';
import Memes from '../views/other/Memes.vue';

//Contact
import ContactMe from '../views/Contact.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: Home
        },
        {
            path: '/apply',
            component: WhereToApply
        },
        {
            path: '/jobs/WhereToApply',
            component: WhereToApply
        },
        {
            path: '/jobs/ResumeTemplate',
            component: ResumeTemplate
        },
        {
            path: '/jobs/OffersRecieved',
            component: OffersRecieved
        },
        {
            path: '/jobs/InterviewTips',
            component: InterviewTips
        },
        {
            path: '/jobs/HelpfulWebsites',
            component: HelpfulWebsites
        },
        {
            path: '/jobs/JobTips.vue',
            component: JobTips
        },
        {
            path: '/linkedin/WhatIsLinkedin',
            component: WhatIsLinkedin
        },
        {
            path: '/linkedin/SetupProfile',
            component: SetupProfile
        },
        {
            path: '/linkedin/SetupJobAlerts',
            component: SetupJobAlerts
        },
        {
            path: '/linkedin/LinkedinTips',
            component: LinkedinTips
        },
        {
            path: '/classes/ClassRecommendations',
            component: ClassRecommendations
        },
        {
            path: '/classes/CSCDescriptions',
            component: CSCDescriptions
        },
        {
            path: '/classes/ClassesIveTaken',
            component: ClassesIveTaken
        },
        {
            path: '/classes/ClassesToAvoid',
            component: ClassesToAvoid
        },
        {
            path: '/CompSci/VisualStudioCode',
            component: VisualStudioCode
        },
        {
            path: '/CompSci/VSCodeSettings',
            component: VSCodeSettings
        },
        {
            path: '/CompSci/VSCodeShortcuts',
            component: VSCodeShortcuts
        },
        {
            path: '/CompSci/FavoriteLibraries',
            component: FavoriteLibraries
        },
        {
            path: '/CompSci/CompSciTips',
            component: CompSciTips
        },
        {
            path: '/other/GeneralTips',
            component: GeneralTips
        },
        {
            path: '/other/AppsToDownload',
            component: AppsToDownload
        },
        {
            path: '/other/CompSciStuff',
            component: CsStuffILike
        },
        {
            path: '/other/TerminalCommands',
            component: TerminalCommands
        },
        {
            path: '/other/Memes',
            component: Memes
        },
        {
            path: '/ContactMe',
            component: ContactMe
        }
    ]
});


export default router