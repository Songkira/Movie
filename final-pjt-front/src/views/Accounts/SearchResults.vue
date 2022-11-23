<template>
  <span class="card text-bg-dark" style="position: relative; width: 150px; margin: 0.5%;" @click="detailGo">
    <img :src="image_url" class="card-img" alt="..." style="width: 150px;">
    <div class="card-img-overlay" style="width:150px;">
      <!-- <i @click="likes" class="fa-regular fa-circle-xmark fa-xl" style="position: absolute; right: 3%;"></i> -->
      <i style="position: absolute; right: 1%; top: -0.5%; margin: 2%;" @click="likes" class="fa-solid fa-heart fa-2x"></i>
      <h5 class="card-title">{{ movie.title }}</h5>
    </div>
  </span>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'SearchResults',
  props: {
    movie: Object,
  },
  data() {
    return {
      image_url: `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.movie.poster_path }`
    }
  },
  methods: {
    detailGo() {
      this.$emit('selectmv', this.movie)
    },
    likes() {
      if (this.$store.state.token != '') {
          axios({
            method: 'post',
            url: `${API_URL}/movies/${this.movie.id}/${this.$store.state.userid}/likes/`,
          })
            .then(res => {
              this.$emit('nolike')
              console.log(res)
            })
            .catch(err => {
              console.log(err)
            })
          }
    },
  }
}
</script>

<style>

</style>