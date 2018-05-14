import Vue from 'vue'
import Router from 'vue-router'
//import HelloWorld from '@/components/HelloWorld'
import Users from '../components/Users'
import test from '../components/test'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/',
      component: Users
    },
    {
      path: '/test',
      component: test
    }
  ]
})
