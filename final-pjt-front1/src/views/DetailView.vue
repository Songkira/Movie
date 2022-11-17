<template>
  <div id="detail" >
    <div class="left">
      <div>
        <img :src="image_url" class="card-img-top" alt="movie_image">
      </div>
      <div>
        <p>{{ movie?.title }}</p>
        <!-- <p>{{ movie?. }}</p> -->
        <p>국가: {{ movie?.production_countries }}</p>
      </div>
      <div>
        <p>{{ movie?.overview }}</p>
      </div>
    </div>
    <div class="right">
      <div id="star-graph" style="padding: 5px 0px 5px; height: 25%; background-color: antiquewhite;">
        <span class="box" style="background-color:azure">

        </span>
        <span class="box">
          
        </span>
      </div>
      <div id="star-jjim" style="padding: 5px 0px 5px; margin: 1%;height: 15%; background-color: antiquewhite;">
        <span>
          <input type="submit" value="별점 평가하기">
        </span>
        |
        <span>
          <input type="submit" value="찜">  
        </span>
      </div>
      <div id="comment-input" style="padding: 5px 0px 5px; margin: 1%; height: 15%; background-color: antiquewhite;">
        <span>감상평 입력</span>
        <input type="text" v-model.trim="content">
        <button @click="createComment">제출</button>
      </div>
      <div id="comment-box" style="height: 45%; margin: 1%;background-color: antiquewhite;">
        <MyCommentsList
        v-for="(comment, index) of commentlist"
        :key="index"
        :comment="comment"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

import MyCommentsList from '@/views/MyCommentsList'

export default {
  
  name: 'DetailView',
  data() {
    return {
      movie: null,
      image_url: null,
      content: null,
      commentlist: null,
      // username: this.$store.state.username 
    }
  },
  created() {
    this.getMovieDetail()
    this.getCommentDetail()
  },
  components: { MyCommentsList, },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/`
      })
      .then((res) => { 
        // console.log (res)
        this.movie = res.data 
        this.image_url = `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ res.data.poster_path }`
        // this.movie.commentlist = res.data.comment_set
      })
      .catch((err) => { console.log (err) })
    },
    createComment() {
      const content = this.content
      // const movie = this.$route.params.id
      // const id = 
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.id}/comment_create/`,
        data: { content },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        // this.commentlist.push(comment) 
        this.$router.go(this.$router.DetailView)
        // this.$router.push({ name: 'DetailView' })
        // if(this.$route.path!==`/${this.$route.params.id}`)
        // this.$router.push(`/${this.$route.params.id}`)
        // this.comment = null
      })
      .catch((err => {
        console.log(err)
      }))
    },
    getCommentDetail() {
      // const id = $route.params.id
      axios({
        method: 'get',
        url: `${API_URL}/movies/commentlist/`
      })
      .then((res) => { 
        console.log(res)
        // if ( id === movie_id )
        this.commentlist = res.data
      })
      .catch((err) => { console.log (err) })
    },
  },
}
</script>

<style>
/* div {
  margin: 1%
} */
#detail {
  padding:5% 5% 5% 5%; 
  /* color: white; */
  height: 100vh;
}
.left {
  padding: 10px;
  float: left;
  /* background-color: pink; */
  width: 30%;
}
.right {
  padding: 10px;
  float: right;
  /* background-color: skyblue; */
  width: 70%;
}
/* .right > div {
  
} */
#star-jjim {
  display : flex; 
  justify-content : space-around;
}
</style>