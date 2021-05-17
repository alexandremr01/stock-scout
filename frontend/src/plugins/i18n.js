import Vue from 'vue'
import VueI18n from 'vue-i18n';

Vue.use(VueI18n);
const messages = {
    'en': {
        'pageNotFound': "Page Not Found",
        'backToHome': "Back to home"
    },
    'pt-br': {
        'pageNotFound': "Página Não Encontrada",
        'backToHome': "Voltar ao início"
    }
};

export default new VueI18n({
    locale: 'en', // set locale
    fallbackLocale: 'es', // set fallback locale
    messages, // set locale messages
});