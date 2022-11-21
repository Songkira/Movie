<template>
  <div>
    <div class="card" style="height: auto;">
      <div class="card-body" style="display: flex; width:100%; height:auto; background-color: #2c3e50;">
        <span class="row-12 col-2" style="background-color: #161e27; border-radius: 4px;">
          <img id="personimg" :src="require(`@/assets/user.jpg`)" style="width:60%; margin: 10%;">
          <br>
          <h5 @click="mypageGo"><b>{{ comment.username }}</b></h5>
        </span>
        <span class="col-8" style="margin: 5%;">
          <h6>{{ comment.content }}</h6>
        </span>
        <span class="col-1">
          <i @click="deleteComment" class="fa-solid fa-xmark"></i>
        </span>
      </div>
    </div>
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
        this.$router.go(this.$router.MovieCommentsList)
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
#personimg {
  border-radius: 70%;
}
</style>