import Vue from 'vue'
import App from './App.vue'
// import todo from './components/todo.vue'



Vue.config.productionTip = false

new Vue({
  render: h => h(App)
}).$mount('#app')
