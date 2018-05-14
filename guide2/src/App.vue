<template>
  <div id="app">
    <router-view/>
    <todo-item v-for="item in groceryList"
               v-bind:todo="item"
               v-bind:key="item.id">

    </todo-item>
  </div>
</template>

<script>
  export default {
    name: 'App',
    data: function () {
      return {
        groceryList: [
          {id: 0, text: "Vegetables"},
          {id: 1, text: "Cheese"},
          {id: 2, text: "Whatever else"}
        ]
      }
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    /*text-align: center;*/
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
