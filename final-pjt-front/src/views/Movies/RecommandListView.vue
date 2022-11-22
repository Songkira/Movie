<template>
  <div class='first col-3'>
    <router-link :to="{ name: 'DetailView', params: { id: item.id }}">
      <div class="card" style="background-color: #161e27; width: 220px; color: white; display: inline-block; margin: 3%;" @mouseenter="selectCard" @mouseleave="selectCard">
        <img :src="image_url" class="card-img-top" alt="movie_image">
        <div class="card-body" style="border: 1px solid #161e27;">
          <h6 class="card-title"><b>{{ item.title }}</b></h6>
          <span v-for="genre in movie_genres" :key="genre.id">
            <span class="badge text-bg-light" style="margin: 2%;">{{ genre.name }}</span>
          </span>
          <small class="card-text" style="text-align: justify; width:100%; overflow: hidden; text-overflow: ellipsis;">{{ item.overview }}</small>
          <small>{{item.popularity}}</small>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'RecommandListView',
  data() {
    return {
      image_url: `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.item.poster_path }`,
      movie_genres: []
    }
  },
  props: {
    item: Object,
  },
  created() {
    this.getMovieDetail()
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
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.item.id}/`
      })
      .then((res) => {
        console.log(res)
        this.movie_genres = res.data.genres
        console.log(this.movie_genres)
      })
      .catch((err) => { console.log (err) })
    },
  }
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
  height: 230px;
  background-color: rgba(255, 255, 255, 0.1);
 }
</style>