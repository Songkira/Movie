<template>
  <div class='first col-4 col-md-3 col-xl-2'>
    <router-link :to="{ name: 'DetailView', params: { id: movie.id }}">
      <div class="card" style="background-color: #161e27; width:100%; color: white; display: inline-block; margin: 3%;" @mouseenter="selectCard" @mouseleave="selectCard">
        <img :src="image_url" class="card-img-top" alt="movie_image">
        <div class="card-body" style="border: 1px solid #161e27;">
          <h5 class="card-title"><b>{{ movie.title }}</b></h5>
          <span v-for="genre in movie.genres" :key="genre.id">
            <span v-if="genre.id === 27" class="badge text-bg-danger" style="margin: 2%;">{{ genre.name }}</span>
            <span v-else-if="genre.id === 28 || genre.id === 53 || genre.id === 80" class="badge text-bg-warning" style="margin: 2%;">{{ genre.name }}</span>
            <span v-else class="badge text-bg-light" style="margin: 2%;">{{ genre.name }}</span>
          </span>
          <br>
          <p class="card-text" style="text-align: justify; width:100%; overflow: hidden; text-overflow: ellipsis;">{{ movie.overview }}</p>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
// import axios from 'axios'

// const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  data() {
    return {
      image_url: `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.movie.poster_path }`
    }
  },
  created() {
    // this.getMovieDetail()
  },
  methods: {
    selectCard(event) {
      const card_index = event.target
      if (card_index.style.color === 'pink') {
        card_index.style.color = 'white'
      } else {
        card_index.style.color = 'pink'
      }
    },
  },
}
</script>

<style>
 .first{
  margin: 2%;
 }
 .card-text{
  overflow: hidden; 
  text-overflow: ellipsis;
  white-space: normal;
  display: -webkit-box;
  -webkit-line-clamp: 5; 
  -webkit-box-orient: vertical;
  width: 250px;
 }
 .card-title {
  overflow: hidden; 
  text-overflow: ellipsis;
  white-space: normal;
  display: -webkit-box;
  -webkit-line-clamp: 1; 
  -webkit-box-orient: vertical;
 }
 .card-body{
  width: 100%;
  height: 200px;
  background-color: rgba(255, 255, 255, 0.1);
 }
</style>