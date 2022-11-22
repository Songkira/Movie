<template>
  <div class="card text-bg-dark col-2" style="position: relative; margin: 2%;">
    <img :src="image_url" class="card-img" alt="..." style="width: 100%;" @click="detailGo">
    <div class="card-img-overlay" @click="detailGo">
      <!-- <i @click="likes" class="fa-regular fa-circle-xmark fa-xl" style="position: absolute; right: 3%;"></i> -->
      <!-- <h5 class="card-title">{{ movie.title }}</h5> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'FollowerLikesList',
  props: {
    likemovie: Object
  },
  data() {
    return {
      image_url: `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.likemovie.poster_path }`
    }
  },
  methods: {
    detailGo() {
      this.$router.push({ name:"DetailView", params: { id: this.likemovie.id } })
    },
  }
}
</script>

<style>

</style>