import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import store from '@/store.js';

Vue.use(Router);

const router = new Router({
    mode: 'history',
    base: '',
    routes: [
        {
            path: '/home',
            name: 'home',
            component: () => import('./views/Home.vue'),
        },
        {
            path: '/simulations',
            name: 'simulation',
            component: () => import('./views/Simulations.vue'),
            meta: {
                authRequired: true
            }
        },
        {
            path: '/about',
            name: 'about',
            component: () => import('./views/About.vue'),
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('./views/Dashboard.vue')
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('./views/Login.vue')
        },
        {
            path: '/sign-up',
            name: 'signup',
            component: () => import('./views/Signup.vue')
        },
        {
            path: '/',
            name: 'welcome',
            component: () => import('./views/Welcome.vue')
        },
        {
            path: '*',
            name: 'not-found',
            component: () => import('./views/NotFound.vue')
        },
    ]
});
router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.authRequired)) {
        if (!store.getters.isLoggedIn) {
            next({
                path: '/'
            });
        } else {
            next();
        }
    } else {
        next();
    }
});
export default router;