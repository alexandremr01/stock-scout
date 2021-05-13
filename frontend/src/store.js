import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        token: localStorage.getItem('t'),
        user: "Usuario"
    },
    mutations: {
        updateToken(state, newToken){
            localStorage.setItem('t', newToken);
            state.token = newToken;
        },
        removeToken(state){
            localStorage.removeItem('t');
            state.token = null;
        }
    },
    getters : {
        isLoggedIn: state => state.token != null,
        authStatus: state => state.status,
    },
    actions: {

    }
})