<template>
  <div id="app">
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
      <div class="container-fluid">
        <img class="navbar-brand" type="button" :src="require(`./assets/logo.png`)" alt="" style="width: 10%;" @click="homeGo">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" style="justify-content: right;" id="navbarNavDropdown" >
          <ul class="navbar-nav">
            <li v-if="this.$store.getters.isLogin === true" class="nav-item" style="margin:auto;">
              <router-link class="nav-link" :to="{ name: 'MovieView' }"><b>Movies</b></router-link>
            </li>
            <li v-if="this.$store.getters.isLogin === true" class="nav-item" style="margin:auto;">
              <router-link class="nav-link" :to="{ name: 'RecommendView' }"><b>Recommend</b></router-link>
            </li>
            <li v-if="this.$store.getters.isLogin === true" class="nav-item" style="margin:auto;">
              <router-link class="nav-link" :to="{ name: 'RandomView' }"><b>Random</b></router-link>
            </li>
            <li v-if="this.$store.getters.isLogin === false" class="nav-item" style="margin:auto;">
              <router-link class="nav-link" :to="{ name: 'SignUp' }"><b>SignUp</b></router-link>
            </li>
            <li v-if="this.$store.getters.isLogin === false" class="nav-item" style="margin:auto;">
              <router-link class="nav-link" :to="{ name: 'Login' }"><b>Login</b></router-link>
            </li>
            <li v-if="this.$store.getters.isLogin === true" class="nav-item" style="margin:auto;">
              <router-link class="nav-link" :to="{ name: 'Login' }"><b>Logout</b></router-link>
            </li>
            
            <li v-if="this.$store.getters.isLogin === true && this.catnumber !== 0" class="nav-item dropdown" style="width:150px; margin: auto;">
              <a class="nav-link dropdown-toggle" role="button" href="" data-bs-toggle="dropdown" aria-expanded="false">
                <img id="personimg" :src="require(`./assets/catpic/cat_ (${catnumber}).jpg`)" style="width:28%; margin-right: 3%;">
                <!-- <img id="personimg" :src="require(usercatpic)" style="width:25%; margin-right: 3%;"> -->
                <b>ID: {{ this.$store.state.username }}</b>
              </a>
              <ul class="dropdown-menu bg-dark">
                <li>
                  <router-link class="dropdown-item" style="color: white;" :to="{ name: 'MyPage', params: { personname: this.$store.state.username } }">MyPage</router-link>
                </li>
                <li>
                  <router-link class="dropdown-item" style="color: white;" :to="{ name: 'MySettings' }">My settings</router-link>
                </li>
              </ul>
            </li>
          </ul>
          <i class="fa-solid fa-magnifying-glass fa-2x" style="margin: 1%;" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal"></i>
        </div>
      </div>
    </nav>
    <router-view
    :key="$route.fullPath"/>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h3 class="modal-title fs-5" style="color: black;" id="exampleModalLabel">영화 검색</h3>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="close"></button>
          </div>
          <div class="modal-body" @submit.prevent="searchMovie">
            <form class="d-flex" role="search">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model.trim="searchword" @keyup="wordchange">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
            <div style="display: flex; flex-wrap: wrap;">
              <SearchResults
              v-for="movie in results"
              :key="movie.id"
              :movie="movie"
              data-bs-dismiss="modal" aria-label="Close"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchResults from '@/views/Movies/SearchResults.vue'
export default {
  name: 'App',
  components: {
    SearchResults
  },
  data() {
    return {
      isLogin: this.$store.getters.isLogin,
      searchword: '',
      results: [],
    }
  },
  created() {
    this.movieGet()
    // this.catnumber = this.$store.state.usercatpic
    console.log(this.$store.state.usercatpic)
  },
  computed: {
    catnumber() {
      return this.$store.state.usercatpic
    }
  },
  watch: {
    searchword(word) {
      console.log(word)
    }
  },
  methods: {
    movieGet() {
      this.$store.dispatch('movieGet')
    },
    wordchange(event) {
      this.searchword = event.target.value
      // console.log(this.searchword, typeof(this.searchword))
      this.searchMovie()
    },
    close() {
      this.searchword = ''
      this.results = []
    },
    searchMovie() {
      if (this.searchword.length !== 0) {
        const word = this.searchword
        const base = this.$store.state.movies
        const rst = []
        for (let i=0; i<base.length; i++) {
          if (base[i].title.includes(word)) {
            rst.push(base[i])
          } else if (base[i].overview.includes(word)) {
            rst.push(base[i])
          }
        }
        this.results = rst
      } else {
        this.results = []
      }
    },
    homeGo() {
      this.$router.push({ name: 'HomeView' })
    }
  }
}
</script>
<style>
#app {
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-size:cover;
}

</style>
