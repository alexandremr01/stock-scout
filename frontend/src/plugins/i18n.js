import Vue from 'vue'
import VueI18n from 'vue-i18n';

Vue.use(VueI18n);
const messages = {
    'en': {
        'pageNotFound': "Page Not Found",
        'backToHome': "Back to home",
        'login': "Login",
        'signup': "Signup",
        'guest': "Join as Guest",
        'join': "Join us!",
        'back': "Back",
    },
    'pt-br': {
        'pageNotFound': "Página Não Encontrada",
        'backToHome': "Voltar ao início",
        'login': "Entrar",
        'signup': "Registrar",
        'guest': "Entre como convidado",
        'join': "Junte-se a nós!",
        'back': "Voltar",
    }
};

export default new VueI18n({
    locale: 'en', // set locale
    fallbackLocale: 'pt-br', // set fallback locale
    messages, // set locale messages
});