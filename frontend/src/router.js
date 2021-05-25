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
            component: Home,
            meta: {
                authRequired: true
            }
        },
        {
            path: '/simulations',
            name: 'simulation',
            component: () => import('./views/Simulations.vue'),
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
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('./views/Dashboard.vue'),
            meta: {
                authRequired: true
            }
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
            name: 'join',
            component: () => import('./views/Join.vue')
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