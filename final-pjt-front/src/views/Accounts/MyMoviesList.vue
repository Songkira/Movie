<template>
  <div class="card text-bg-dark" @click="detailGo">
    <img :src="image_url" class="card-img" alt="..." style="width: 150px;">
    <div class="card-img-overlay">
      <br>
      <br>
      <!-- <h5 class="card-title">{{ movie.title }}</h5> -->
    </div>
  </div>
</template>

<script>
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
    }
  }
}
</script>

<style>

</style>