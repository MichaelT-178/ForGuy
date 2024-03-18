import { createRouter, createWebHistory } from 'vue-router';

//Home 
import Home from '../views/Home.vue';

//Jobs 
import WhereToApply from '../views/jobs/WhereToApply.vue';
import ResumeTemplate from '../views/jobs/ResumeTemplate.vue';
import HowToGetAJob from '../views/jobs/HowToGetAJob.vue'
import OffersReceived from '../views/jobs/OffersReceived.vue';
import InterviewTips from '../views/jobs/InterviewTips.vue';
import CareerPathAdvice from '../views/jobs/CareerPathAdvice.vue';

//Linkedin 
import WhatIsLinkedin from '../views/linkedin/WhatIsLinkedin.vue';
import SetupProfile from '../views/linkedin/SetupProfile.vue';
import SetupJobAlerts from '../views/linkedin/SetupJobAlerts.vue';
import LinkedinTips from '../views/linkedin/LinkedinTips.vue';
import Contacts from '../views/linkedin/Contacts.vue';

//Classes 
import ClassRecommendations from '../views/classes/ClassRecommendations.vue';
import CSCDescriptions from '../views/classes/CSCDescriptions.vue';
import ClassesIveTaken from '../views/classes/ClassesIveTaken.vue';
import ClassesToAvoid from '../views/classes/ClassesToAvoid.vue';
import CompSciMinor from '../views/classes/CompSciMinor.vue';
import Certifications from '../views/classes/Certifications.vue';

//Comp Sci
import VisualStudioCode from '../views/compsci/VisualStudioCode.vue';
import GitHubView from '../views/compsci/GitHub.vue';
import VSCodeSettings from '../views/compsci/VSCodeSettings/VSCodeSettings.vue';
import VSCodeExtensions from '../views/compsci/VSCodeExtensions.vue';
import VSCodeShortcuts from '../views/compsci/VSCodeShortcuts.vue';
import UIDesignTips from '../views/compsci/UIDesignTips.vue';
import CompSciTips from '../views/compsci/CompSciTips.vue';

//Other 
import GeneralTips from '../views/other/GeneralTips.vue';
import AppsToDownload from '../views/other/AppsToDownload.vue';
import CsStuffILike from '../views/other/CsStuffILike.vue';
import TerminalCommands from '../views/other/TerminalCommands.vue';
import KeyboardShortcuts from '../views/other/KeyboardShortcuts.vue';
import Memes from '../views/other/Memes.vue';
import UncwPics from '../views/other/UncwPictures.vue';

//Contact
import ContactMe from '../views/Contact.vue'

//Image View to display images
import ImageView from '../views/ImageView.vue';

//Search Results view for when return in pressed when the SearchBar is open
import SearchResults from '../views/SearchResults.vue';


//The routes 
const routes = [
    {
        path: '/',
        component: Home
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
        path: '/jobs/OffersReceived',
        component: OffersReceived
    },
    {
        path: '/jobs/InterviewTips',
        component: InterviewTips
    },
    {
        path: '/jobs/HowToGetAJob.vue',
        component: HowToGetAJob
    },
    {
        path: '/jobs/CareerPathAdvice',
        component: CareerPathAdvice
    },
    {
        path: '/linkedin/WhatIsLinkedIn',
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
        path: '/linkedin/Contacts',
        component: Contacts
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
        path: '/classes/CompSciMinor',
        component: CompSciMinor
    },
    {
        path: '/classes/Certifications',
        component: Certifications
    },
    {
        path: '/CompSci/VisualStudioCode',
        component: VisualStudioCode
    },
    {
        path: '/CompSci/GitHub',
        component: GitHubView
    },
    {
        path: '/CompSci/VSCodeSettings',
        component: VSCodeSettings
    },
    {
        path: '/CompSci/VSCodeExtensions',
        component: VSCodeExtensions
    },
    {
        path: '/CompSci/VSCodeShortcuts',
        component: VSCodeShortcuts
    },
    {
        path: '/CompSci/UIDesignTips',
        component: UIDesignTips
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
        path: '/other/KeyboardShortcuts',
        component: KeyboardShortcuts
    },
    {
        path: '/other/Memes',
        component: Memes
    },
    {
        path: '/other/UncwPics',
        component: UncwPics
    },
    {
        path: '/ContactMe',
        component: ContactMe
    },
    {
        path: '/image-view/:Name/:Description/:Pic',
        name: 'ImageView',
        component: ImageView,
        props: true
    },
    {
        path: '/SearchResults/:SearchQuery',
        name: 'SearchResults',
        component: SearchResults,
        props: true
    }
]

const router = createRouter({
    history: createWebHistory('/'),
    routes
});

export default router