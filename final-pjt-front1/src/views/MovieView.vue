<template>
  <div id="MovieView">
    <MovieCard v-for="(movie, index) in movies" :key="index" :movie="movie"
    />
  </div>
</template>

<script>
import MovieCard from '@/views/MovieCard.vue'

export default {
  name: 'MovieView',
  components: {
    MovieCard
  },
  computed: {
    movies() { return this.$store.state.movies }
  }
}
</script>

<style>
#MovieView {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  height: 100%;
}

</style>