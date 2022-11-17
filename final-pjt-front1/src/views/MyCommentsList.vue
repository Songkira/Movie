<template>
  <div>
    <span>{{ comment.content }}</span>
    <button @click="deleteComment">x</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MyCommentsList',
  props: {
    comment: Object,
  },
  methods: {
    deleteComment() {
      axios({
        method: 'delete',
        url:`${API_URL}/movies/${this.comment.id}/comment_detail`
      })
      .then((res) => {
        console.log(res)
        this.comment.delete()
      })
      .catch((err) => {
        console.log(err)
      })
      // const index = this.comment.indexOf(this.comment)
      // this.comment.splice(index, 1)
      // this.comment = 
    },
    // updateComment() {
    //   this.$store.dispatch('updateComment', this.comment)
    // },
  }, 
}
</script>

<style>

</style>