<template>
  <div>
    <img :src="image_url" alt="" >
    {{ item.title }}
  </div>
</template>

<script>
export default {
  name: 'RecommandListView',
  data() {
    return {
      image_url: `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.item.poster_path }`
    }
  },
  props: {
    item: Object,
  },
  methods: {

  }
}
</script>

<style>

</style>