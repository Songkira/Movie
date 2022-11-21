<template>
  <div id="app">
    <br>
    <button type="button" class="btn btn-light" @click="randomMovie">PICK</button>
    <div style="display: flex; justify-content: center;">
      <div class="card mb-3" style="max-width: 750px; max-height: 380px;" v-if="movie">
        <div class="row g-0" style="height: 100%;">
          <div class="col-md-4" style="height: 100%;">
            <img :src="randomImage" class="img-fluid rounded-start" style="height: 100%;" alt="">
          </div>
          <div class="card-body col-md-8" style="height: 100%;">
            <br>
            <h5 class="card-title"><b>{{ movie?.title }}</b></h5>
            <p class="card-title">평점: {{ movie?.vote_average }}</p>
            <br>
            <span style="display: flex; justify-content: center; text-align: left;">
              <p id="randomoverview" class="card-text">{{ movie?.overview }}</p>
            </span>
          </div>
        </div>
      </div>
    </div>
    <!-- <div style="height: 50%; display: flex; justify-content: center;">
      <div class="card" style="width: 30%; background-color: #161e27; color: white;" v-if="movie">
        <img :src="randomImage" alt="">
        <div style="margin:1%; width: auto;">
        <h4 style="margin: 10%;" ><b>{{ movie?.title }}</b></h4>
        <h5>평점: {{ movie?.vote_average }}</h5>
        </div>
      </div>
    </div> -->
    <p></p>
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
  background-size: cover;
  height: 100%;
}
.card {
  margin: 3%;
  background-color: #161e27;
}
#randomoverview {
  overflow: hidden; 
  text-overflow: ellipsis;
  white-space: normal;
  display: -webkit-box;
  -webkit-line-clamp: 7; 
  -webkit-box-orient: vertical;
  width: 400px;
 }
</style>