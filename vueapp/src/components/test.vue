<template>
  <div class="test">
    <input type="text" v-model="title">
    <h1>{{title}}</h1>
    <p v-if="showName">{{user.firstName}}</p>
    <p v-else>Nobody</p>
    <ul>
      <li v-for="item in items">{{item.title}}</li>
    </ul>
    <button v-on:click="greet(title)">Say Greeting</button>
    <br/>
    <input type="text" v-on:keyup="pressKey" v-on:keyup.enter="enterHit">
    <hr/>
    <input type="text" v-model="user.firstName">
    <br/>
    <input type="text" v-model="user.lastName">
    <h1>{{fullName}}</h1>
    <hr/>
    <h2>{{msg}}</h2>
  </div>
</template>

<script>
  export default {
    name: 'test',
    props: {
      msg: {
        type: String,
        default: "Default Message"
      }

    },
    data() {
      return {
        title: "Hello world!",
        user: {
          firstName: "John",
          lastName: "Doe"
        },
        showName: true,
        items: [
          {title: 'Item One'},
          {title: 'Item Two'},
          {title: 'Item Three'}
        ]
      }
    },
    methods: {
      greet: function(greeting) {
        alert(greeting);
      },
      pressKey: function(event) {
        console.log(event.target.value);
      },
      enterHit: function(event) {
        console.log("You hit enter.");
      }
    },
    computed: {
      fullName: function() {
        return this.user.firstName + ' ' + this.user.lastName;
      }
    }
  }
</script>

<style scoped>
</style>
