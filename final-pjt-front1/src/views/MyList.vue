<template>
  <div>
    <h1>내가 찜한 영화</h1>
    <MyMoviesList/>
    <h1>내가 평가한 영화</h1>
    <MyCommentsList/>
  </div>
</template>

<script>
import MyMoviesList from '@/views/MyMoviesList.vue'
import MyCommentsList from '@/views/MyCommentsList.vue'
export default {
    name: 'MyList',
    components: {
        MyMoviesList,
        MyCommentsList,
    }
}
</script>

<style>

</style>