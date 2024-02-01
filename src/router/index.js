import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Cool from '../views/Cool.vue'
import VSCodeSettingsView from '../views/VSCodeSettings.vue'
import WhereToApply from '../views/jobs/WhereToApply.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: Home
        },
        {
            path: '/about',
            component: About
        },
        {
            path: '/cool',
            component: Cool
        },
        {
            path: '/apply',
            component: WhereToApply
        },
        {
            path: '/settings',
            component: VSCodeSettingsView
        }
    ]
});


export default router