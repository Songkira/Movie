<template>
  <span class="card text-bg-dark" style="position: relative; width: 150px; margin: 0.5%;" @click="selected">
    <img :src="image_url" class="card-img" alt="..." style="width: 150px;">
    <div class="card-img-overlay" style="width:150px;">
      <!-- <i @click="likes" class="fa-regular fa-circle-xmark fa-xl" style="position: absolute; right: 3%;"></i> -->
      <!-- <i style="position: absolute; right: 1%; top: -0.5%; margin: 2%;" @click="likes" class="fa-solid fa-heart fa-2x"></i> -->
      <!-- <h5 class="card-title">{{ movie.title }}</h5> -->
    </div>
  </span>
</template>

<script>
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
    selected() {
      this.$router.push({ name:"DetailView", params: { id: this.movie.id } })
    },
  }
}
</script>

<style>

</style>