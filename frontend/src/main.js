import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import router from './router';
import store from './store';
import i18n from '@/plugins/i18n';
import FlagIcon from 'vue-flag-icon';
import './registerServiceWorker'

Vue.use(FlagIcon);
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.use(VueResource)

Vue.config.productionTip = false

export const bus = new Vue();

new Vue({
  i18n,
  router,
  render: h => h(App),
  store
}).$mount('#app')
