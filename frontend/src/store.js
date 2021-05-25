import Vue from 'vue';
import Vuex from 'vuex';
import jwt_decode from 'jwt-decode';
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
            state.user = jwt_decode(newToken).username
        },
        removeToken(state){
            localStorage.removeItem('t');
            state.token = null;
        }
    },
    getters : {
        isLoggedIn: state => (state.token != null && jwt_decode(state.token).exp*1000 > new Date().getTime()),
        authStatus: state => state.status,
    },
    actions: {

    }
})