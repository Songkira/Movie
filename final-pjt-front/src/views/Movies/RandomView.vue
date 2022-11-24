<template>
  <div id="app">
    <br>
    <button type="button" class="btn btn-light col-6 animate__animated animate__headShake" v-if="first" @click="randomMovie">PICK</button>
    <div style="display: flex; justify-content: center; margin: 5%;" v-if="this.movie !== null">
      <div class="card mb-3 col-10 col-xs-8 col-xl-6 animate__animated animate__tada" style="max-width: 750px; max-height: 380px;" @click="detailGo" @mouseenter="selectCard" @mouseleave="selectCard">
        <div class="row g-0" style="height: 100%;">
          <div class="col-md-4" style="height: 100%;">
            <img :src="randomImage" class="img-fluid rounded-start" style="height: 100%;" alt="">
          </div>
          <div class="card-body col-md-8" style="height: 100%; background-color: #161e27;">
            <br>
            <h5 class="card-title"><b>{{ movie?.title }}</b></h5>
            <span v-for="genre in this.movie.genres" :key="genre.id">
              <span v-if="genre.id === 27" class="badge text-bg-danger" style="margin: 2%;">{{ genre.name }}</span>
              <span v-else-if="genre.id === 28 || genre.id === 53 || genre.id === 80" class="badge text-bg-warning" style="margin: 2%;">{{ genre.name }}</span>
              <span v-else class="badge text-bg-light" style="margin: 2%;">{{ genre.name }}</span>
            </span>
            <p class="card-title">평점: {{ movie?.vote_average }}</p>
            <br>
            <span style="display: flex; justify-content: center; text-align: left;">
              <p id="randomoverview" class="card-text">{{ movie?.overview }}</p>
            </span>
          </div>
        </div>
      </div>
    </div>
    <button type="button" class="btn btn-light col-6" v-if="movie !== null" @click="randomMovie2">다시하기</button>
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
      first: true,
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
      this.first = false
    },
    randomMovie2() {
      this.movie = null
      this.$router.go({ name:"RandomView" })
    },
    detailGo() {
      this.$router.push({ name:"DetailView", params: { id: this.movie.id } })
    },
    selectCard(event) {
      const card_index = event.target
      if (card_index.style.color === 'pink') {
        card_index.style.color = 'white'
      } else {
        card_index.style.color = 'pink'
      }
    },
  }

}
</script>

<style>
#app {
  background-size: cover;
  height: 100%;
}
.card-body {
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