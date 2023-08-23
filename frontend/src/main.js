import Vue from 'vue';
import App from './App.vue';
import 'chart.js';
import 'vue-chartjs';
import 'chartjs-plugin-annotation';
import '@/assets/scss/app.scss';
import './plugins/bootstrap-vue';
Vue.config.productionTip = false;
import i18n from './i18n';
new Vue({
  i18n,
  render: (h) => h(App),
}).$mount('#app');
