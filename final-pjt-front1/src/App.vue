<template>
  <div id="app">
    <nav class="nav justify-content-end">
      <h3 style="color: white;">안녕하세요. {{ this.$store.state.username }} 님.</h3>
      <router-link :to="{ name: 'MovieView' }">Movie</router-link>&nbsp;&nbsp;
      <router-link :to="{ name: 'RandomView' }">Random</router-link>&nbsp;&nbsp;
      <router-link :to="{ name: 'WatchListView' }">WatchList</router-link>&nbsp;&nbsp;
      <router-link :to="{ name: 'MyPage', params: { personname: this.$store.state.username } }">MyPage</router-link>&nbsp;&nbsp;
      <router-link :to="{ name: 'SignUp' }">SignUp</router-link>&nbsp;&nbsp;
      <router-link :to="{ name: 'Login' }">Login</router-link>&nbsp;&nbsp;
      <a @click="getUsers">test3</a>&nbsp;&nbsp;
      <a @click="logOut">Logout</a>&nbsp;&nbsp;
    </nav>
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
const personname = 'test1'
export default {
  name: 'App',
  created() {
    this.movieGet()
    // this.username = this.$store.state.username
  },
  methods: {
    movieGet() {
      this.$store.dispatch('movieGet')
    },
    logOut() {
      this.$store.dispatch('logOut')
    },
    getUsers() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts-custom/usersinfo/`,
      })
        .then(res => {
          const prmts = { pk: -1, personname: null }
          console.log(res)
          for (let i=0; i < res.data.length; i++) {
            if (res.data[i].username === personname) {
              prmts.pk = res.data[i].id
              prmts.personname = res.data[i].username
              break
            }
          }
          console.log(prmts)
          this.$router.push({name: 'MyPage', params: prmts})
          console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-color: #2c3e50;
  height: 100vh;
}

nav {
  padding: 30px;
  background-color: #1f242a;
}

nav a {
  font-weight: bold;
  color: white;
  word-spacing: 20px;
}

nav a.router-link-exact-active {
  color: #42b983;
}
nav router-link {
  padding: 0px 20px;
}
</style>
