
<template>
  <div id="app-5">
    <p>{{message}}</p>
    <button v-on:click="reverseMessage">Reverse Message</button>
    <input v-model="message">
    <todoitem></todoitem>
  </div>
</template>


<script>

import todoitem from "./components/todo.vue";

export default {
  name: 'app',
  //el = '#app-5',
  components: {
    todoitem
  },
  data: function() {
    return {
      message: 'Hello Vue.js!'
    }
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
