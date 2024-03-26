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
import Memes from '../views/other/memes.vue';
import UncwPics from '../views/other/UncwPictures.vue';

//Contact
import ContactMe from '../views/contact.vue'

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
        path: '/Jobs/WhereToApply',
        component: WhereToApply
    },
    {
        path: '/Jobs/ResumeTemplate',
        component: ResumeTemplate
    },
    {
        path: '/Jobs/OffersReceived',
        component: OffersReceived
    },
    {
        path: '/Jobs/InterviewTips',
        component: InterviewTips
    },
    {
        path: '/Jobs/HowToGetAJob.vue',
        component: HowToGetAJob
    },
    {
        path: '/Jobs/CareerPathAdvice',
        component: CareerPathAdvice
    },
    {
        path: '/LinkedIn/WhatIsLinkedIn',
        component: WhatIsLinkedin
    },
    {
        path: '/LinkedIn/SetupProfile',
        component: SetupProfile
    },
    {
        path: '/LinkedIn/SetupJobAlerts',
        component: SetupJobAlerts
    },
    {
        path: '/LinkedIn/LinkedinTips',
        component: LinkedinTips
    },
    {
        path: '/LinkedIn/Contacts',
        component: Contacts
    },
    {
        path: '/Classes/ClassRecommendations',
        component: ClassRecommendations
    },
    {
        path: '/Classes/CSCDescriptions',
        component: CSCDescriptions
    },
    {
        path: '/Classes/ClassesIveTaken',
        component: ClassesIveTaken
    },
    {
        path: '/Classes/ClassesToAvoid',
        component: ClassesToAvoid
    },
    {
        path: '/Classes/CompSciMinor',
        component: CompSciMinor
    },
    {
        path: '/Classes/Certifications',
        component: Certifications
    },
    {
        path: '/compsci/VisualStudioCode',
        component: VisualStudioCode
    },
    {
        path: '/compsci/GitHub',
        component: GitHubView
    },
    {
        path: '/compsci/VSCodeSettings',
        component: VSCodeSettings
    },
    {
        path: '/compsci/VSCodeExtensions',
        component: VSCodeExtensions
    },
    {
        path: '/compsci/VSCodeShortcuts',
        component: VSCodeShortcuts
    },
    {
        path: '/compsci/UIDesignTips',
        component: UIDesignTips
    },
    {
        path: '/compsci/CompSciTips',
        component: CompSciTips
    },
    {
        path: '/Other/GeneralTips',
        component: GeneralTips
    },
    {
        path: '/Other/AppsToDownload',
        component: AppsToDownload
    },
    {
        path: '/Other/CompSciStuff',
        component: CsStuffILike
    },
    {
        path: '/Other/TerminalCommands',
        component: TerminalCommands
    },
    {
        path: '/Other/KeyboardShortcuts',
        component: KeyboardShortcuts
    },
    {
        path: '/Other/Memes',
        component: Memes
    },
    {
        path: '/Other/UncwPics',
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