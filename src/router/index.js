import { createRouter, createWebHistory } from 'vue-router';

//Home 
import Home from '../views/Home.vue';

//Jobs 
import WhereToApply from '../views/Jobs/WhereToApply.vue';
import ResumeTemplate from '../views/Jobs/ResumeTemplate.vue';
import HowToGetAJob from '../views/Jobs/HowToGetAJob.vue'
import OffersReceived from '../views/Jobs/OffersReceived.vue';
import InterviewTips from '../views/Jobs/InterviewTips.vue';
import CareerPathAdvice from '../views/Jobs/CareerPathAdvice.vue';

//Linkedin 
import WhatIsLinkedin from '../views/LinkedIn/WhatIsLinkedin.vue';
import SetupProfile from '../views/LinkedIn/SetupProfile.vue';
import SetupJobAlerts from '../views/LinkedIn/SetupJobAlerts.vue';
import LinkedinTips from '../views/LinkedIn/LinkedinTips.vue';
import Contacts from '../views/LinkedIn/Contacts.vue';

//Classes 
import ClassRecommendations from '../views/Classes/ClassRecommendations.vue';
import CSCDescriptions from '../views/Classes/CSCDescriptions.vue';
import ClassesIveTaken from '../views/Classes/ClassesIveTaken.vue';
import ClassesToAvoid from '../views/Classes/ClassesToAvoid.vue';
import CompSciMinor from '../views/Classes/CompSciMinor.vue';
import Certifications from '../views/Classes/Certifications.vue';

//Comp Sci
import VisualStudioCode from '../views/CompSci/VisualStudioCode.vue';
import GitHubView from '../views/CompSci/GitHub.vue';
import VSCodeSettings from '../views/CompSci/VSCodeSettings/VSCodeSettings.vue';
import VSCodeExtensions from '../views/CompSci/VSCodeExtensions.vue';
import VSCodeShortcuts from '../views/CompSci/VSCodeShortcuts.vue';
import UIDesignTips from '../views/CompSci/UIDesignTips.vue';
import CompSciTips from '../views/CompSci/CompSciTips.vue';

//Other 
import GeneralTips from '../views/Other/GeneralTips.vue';
import AppsToDownload from '../views/Other/AppsToDownload.vue';
import CsStuffILike from '../views/Other/CsStuffILike.vue';
import TerminalCommands from '../views/Other/TerminalCommands.vue';
import KeyboardShortcuts from '../views/Other/KeyboardShortcuts.vue';
import Memes from '../views/Other/memes.vue';
import UncwPics from '../views/Other/UncwPictures.vue';

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