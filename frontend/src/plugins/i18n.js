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
        'monthly': "Monthly contribution",
        'initial': "Initial value",
        'time': "Time - in months",
        'interest': "Annual interest (in %)",
        'final': "Final sum",
        'simulations': 'Simulations',
        'calculate': 'Calculate',
        'save': 'Save',
        'remove': 'Delete',
        'see': 'See',
        'savedSimulations': 'Saved Simulations - Click to restore',
        'errorSimulation': 'Simulation API error',
        'simulationDescription': 'Select the field you want to be calculated and fill the others.'
    },
    'pt-br': {
        'pageNotFound': "Página Não Encontrada",
        'backToHome': "Voltar ao início",
        'login': "Entrar",
        'signup': "Registrar",
        'guest': "Entre como convidado",
        'join': "Junte-se a nós!",
        'back': "Voltar",
        'monthly': "Aporte mensal",
        'initial': "Valor inicial",
        'time': "Tempo - em meses",
        'interest': "Valorização anual (em %)",
        'final': "Acumulado final",
        'simulations': 'Simulações',
        'calculate': 'Calcular',
        'save': 'Salvar',
        'remove': 'Remover',
        'savedSimulations': 'Simulações salvas',
        'see': 'Visualizar',
        'errorSimulation': 'Erro na API de simulação',
        'simulationDescription': 'Selecione o valor que você deseja que seja calculado e digite os demais.'
    }
};

export default new VueI18n({
    locale: 'en', // set locale
    fallbackLocale: 'pt-br', // set fallback locale
    messages, // set locale messages
});