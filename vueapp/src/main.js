// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import vueResource from 'vue-resource';

Vue.config.productionTip = false
Vue.use(vueResource);

/* eslint-disable no-new */
new Vue({
  // el: '#app',
  router,
  template: `
  <div id="app">
  <ul>
  <li><router-link to="/">Users</router-link></li>
  <li><router-link to="/test">Test</router-link></li>
  
</ul>
<router-view></router-view>
  </div>
  `
  // components: { App },
  // template: '<App/>'
}).$mount('#app')
