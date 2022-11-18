<template>
  <div id="app">
    <br>
    <button type="button" class="btn btn-light" @click="randomMovie">PICK</button>
    <div style="height: 100%; display: flex; justify-content: center;">
    <div class="card" style="width: 50%; background-color: #161e27; color: white;" v-if="movie">
      <img :src="randomImage" alt="">
      <div style="margin:1%; width: auto;">
      <h4 style="margin: 10%;" ><b>{{ movie?.title }}</b></h4>
      <h5>평점: {{ movie?.vote_average }}</h5>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'RandomView',
  data() {
    return {
      movie: null,
    }
  },
  computed: {
    movies() { return this.$store.state.movies},
    randomImage() {       
      return `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.movie?.poster_path }`
    },
  },
  methods: {
    randomMovie() {
      this.movie = _.sample(this.movies)
    }
  }

}
</script>

<style>
#app {
  height: 100%;
}
.card {
  margin: 3%;
  background-color: #161e27;
}
</style>