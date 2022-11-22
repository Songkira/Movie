<template>
  <span class="card text-bg-dark" style="position: relative; width: 150px; margin: 0.5%;">
    <img :src="image_url" class="card-img" alt="..." style="width: 150px;" @click="detailGo">
    <div class="card-img-overlay" style="width:150px;">
      <i @click="likes" class="fa-regular fa-circle-xmark fa-xl" style="position: absolute; right: 3%;"></i>
      <!-- <h5 class="card-title">{{ movie.title }}</h5> -->
    </div>
  </span>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'MyMoviesList',
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
      this.$router.push({ name:"DetailView", params: { id: this.movie.id } })
    },
    likes() {
      console.log(this.movie)
      if (this.$store.state.token != '') {
          axios({
            method: 'post',
            url: `${API_URL}/movies/${this.movie.id}/${this.$store.state.userid}/likes/`,
            headers: {
                "Authorization": `Token ${this.$store.state.token}`
              }
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