<template>
  <div style="display: flex; justify-content: center;">
    <span><a @click="mypageGo">{{ comment.username }} -</a></span> 
    <span><h5>{{ comment.content }}</h5></span>
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
      // this.$emit('deletecomment')
      axios({
        method: 'delete',
        url:`${API_URL}/movies/${this.comment.id}/comment_detail/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        console.log(res)
        // this.$router.push({ name: 'DetailView' })
        this.$router.go(this.$router.MyCommentsList)
      })
      .catch((err) => {
        console.log(err)
      }) 
    },
    mypageGo() {
      this.$router.push({ name: 'MyPage', params: { personname: this.comment.username } })
    }
  }, 
}
</script>

<style>

</style>