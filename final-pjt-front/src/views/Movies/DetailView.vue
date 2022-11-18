<template>
  <div id="detail" >
    <div class="left">
      <div>
        <img :src="image_url" class="card-img-top" alt="movie_image">
      </div>
      <div>
        <h4>{{ movie?.title }}</h4>
        <p>국가: {{ movie?.production_countries_name }}</p>
        <h6>{{ movie?.director.name }}</h6>
      </div>
      <span v-for="(genre, idx) in movie.genres" :key="idx">
        <span class="badge text-bg-light" style="margin: 3%;">{{ genre.name }}</span>
      </span>
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
          <select name="rate" v-model="MymovieRate" id="rate">
            <option class="content-font" style="color:black;" :value="rate" v-for="(rate, idx) in this.$store.state.reviewRate" :key="idx">{{ rate }}</option>
          </select>
          <input type="submit" value="별점 평가하기" @click="starRate">
          {{ this.Star === 0 ? this.movie.vote_average: this.Star }}
        </span>
        |
        <span>
          <button @click="likes" type="button" class="btn btn-light">LIKE</button>  
        </span>
      </div>
      <div id="comment-input" style="padding: 5px 0px 5px; margin: 1%; height: 15%; background-color: antiquewhite;">
        <span>감상평 입력</span>
        <input type="text" v-model.trim="content">
        <button @click="createComment">제출</button>
      </div>
      <div id="comment-box" style="height: 45%; margin: 1%;background-color: antiquewhite;">
        <MovieCommentsList
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

import MovieCommentsList from '@/views/Movies/MovieCommentsList'

export default {
  
  name: 'DetailView',
  data() {
    return {
      movie: null,
      image_url: null,
      content: null,
      commentlist: null,
      // username: this.$store.state.username 
      MymovieRate: 0,
      Star: 0,
    }
  },
  created() {
    this.getMovieDetail()
    this.getCommentDetail()
    // this.getStar()
  },
  components: { MovieCommentsList, },
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
        this.getCommentDetail()
        // this.$router.go(this.$router.MyCommentsList)
        // this.$router.push({ name: 'MyCommentsList' })
        this.content = null
      })
      .catch((err => {
        console.log(err)
      }))
    },
    getCommentDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/movie_comment/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => { 
        console.log(res)
        this.commentlist = res.data
      })
      .catch((err) => { console.log (err) })
    },
    starRate() {
      const rank = this.MymovieRate
      const movie = this.movie.id
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.id}/star_test/`,
        data: { rank, movie },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.Star = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getStar() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/star_test/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => { 
        console.log(res.data)
        this.Star = this.movie.vote_average
      })
      .catch((err) => { console.log (err) })
    },
    likes() {
      console.log(this.movie)
      if (this.$store.state.token != '') {
          axios({
            method: 'post',
            url: `${API_URL}/movies/${this.movie.id}/${this.$store.state.userid}/likes/`,
          })
            .then(res => {
              console.log(1112)
              console.log(res)
            })
            .catch(err => {
              console.log(err)
            })
          }
    }
    // deletecomment() {
    //   axios({
    //     method: 'delete',
    //     url:`${API_URL}/movies/${this.$route.params.id}/${this.comment.id}/`,
    //     headers: {
    //       Authorization: `Token ${this.$store.state.token}`
    //     },
    //   })
    //   .then(() => {
    //     // this.$router.go(this.$router.DetailView)
    //     this.getCommentDetail()
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // },
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