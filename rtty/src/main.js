import Vue from 'vue'
import App from './App.vue'
import axios from 'axios';
import ToggleButton from "vue-js-toggle-button";

Vue.use(axios)

export const HTTP = axios.create({
  baseURL: 'http://192.168.0.31:5001',
  headers: {}
})

Vue.use(ToggleButton)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')