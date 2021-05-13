import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';

Vue.use(Router);

const router = new Router({
    mode: 'history',
    // base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/about',
            name: 'about',
            component: () => import('./views/About.vue'),
            meta: {
                authRequired: true
            }
        },
        {
            path: '/sign-in',
            name: 'signin',
            component: () => import('./views/Signin.vue')
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('./views/Dashboard.vue')
        },
    ]
});

export default router;