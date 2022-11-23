<template>
  <div class='first'>
    <router-link :to="{ name: 'DetailView', params: { id: movie.id }}">
      <div class="card text-bg a" style="position: relative; width: 200px; margin: 0.5%; border-color: black;">
        <img :src="image_url" alt="..." class="card-img" style="width: 200px; border-radius: 2%;">
        <div class="card-img-overlay" style="width:200px; background-color: transparent; border-radius: 2%;" @mouseenter="selectCard" @mouseleave="selectCard"
        @mouseover="textoverlay" @mouseout="textoverlay">
          <div class="box" style="visibility: hidden; color:white;" :id="`spo${movie.id}`">
            <p>{{ movie.title }}</p>
            <span v-for="genre in movie.genres" :key="genre.id">
              <span v-if="genre.id === 27" class="badge text-bg-danger" style="margin: 2%;">{{ genre.name }}</span>
              <span v-else-if="genre.id === 28 || genre.id === 53 || genre.id === 80" class="badge text-bg-warning" style="margin: 2%;">{{ genre.name }}</span>
              <span v-else class="badge text-bg-light" style="margin: 2%;">{{ genre.name }}</span>
            </span>
            <p class="card-overview" style=" text-align: justify; width:100%; overflow: hidden; text-overflow: ellipsis;">{{ movie.overview }}</p>
          </div>
        </div>
      </div>
      <!-- <div class="card" style="background-color: #161e27; width:100%; color: white; display: inline-block; margin: 3%;" @mouseenter="selectCard" @mouseleave="selectCard">
        <img :src="image_url" class="card-img-top" style="background-color: #161e27;" alt="movie_image" >
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
      </div> -->
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
      if (card_index.style.backgroundColor === 'transparent') {
        card_index.style.backgroundColor = 'black'
      } else {
        card_index.style.backgroundColor = 'transparent'
      }
    },
    // overlay(event) {
      // // console.log(0)
      // const card_over = event.target
      // if (card_over.style.backgroundColor === 'transparent') {
      //   // console.log(1)
      //   card_over.style.backgroundColor = 'gray'
      // } else {
      //   // console.log(2)
      //   card_over.style.backgroundColor ='transparent'
      // }
    // },
    textoverlay() {
      const tag = document.querySelector(`#spo${this.movie.id}`)
      if (tag.style.visibility === 'visible') {
        console.log('----------------')
        console.log(1)
        tag.style.visibility = 'hidden';
        console.log(tag)
        console.log('-------------')
      } else{
        console.log('=========')
        console.log(2)
        tag.style.visibility = 'visible';
        console.log(tag)
        console.log('=========')
      }
    }
  },
}
</script>

<style>
 .first{
  margin: 2%;
 }
 .card-overview{
  overflow: hidden; 
  text-overflow: ellipsis;
  white-space: normal;
  display: -webkit-box;
  -webkit-line-clamp: 6; 
  -webkit-box-orient: vertical;
  width: 250px;
  font-size: small;
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
  background-color:black;
 }
 .a {
  transition: all 0.2s linear;
}
.a:hover {
  transform: scale(1.1);
}
</style>