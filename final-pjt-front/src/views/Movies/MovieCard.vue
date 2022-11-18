<template>
  <div class='first'>
    <router-link :to="{ name: 'DetailView', params: { id: movie.id }}">
      <div class="card" style="border-color: #161e27; color: white; width: 18rem; display: inline-block; margin: 3%;" @mouseenter="selectCard" @mouseleave="selectCard">
        <img :src="image_url" class="card-img-top" alt="movie_image">
        <div class="card-body">
          <h5><b>{{ movie.title }}</b></h5>
          <br>
          <p class="card-text" style="text-align: justify; overflow: hidden; text-overflow: ellipsis;">{{ movie.overview }}</p>
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
  margin: 1%;
 }
 .card-text{
  overflow: hidden; 
  text-overflow: ellipsis;
  white-space: normal;
  display: -webkit-box;
  -webkit-line-clamp: 7; 
  -webkit-box-orient: vertical;
  width: 250px;
 }
 .card-body{
  height: 250px;
  background-color: #161e27;
 }
</style>