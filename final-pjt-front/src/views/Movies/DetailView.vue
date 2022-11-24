<template>
  <div id="detail" >
    <!-- 영화 디테일 -->
    <div class="col-3 left">
      <div style="position: relative;">
        <img :src="image_url" class="card-img-top" alt="movie_image">
        <i v-if="this.$store.getters.isLogin === true" id="heart" style="position: absolute; left: -0.5%; margin: 2%; color: lightgray;" @click="likes" class="fa-solid fa-heart fa-2x"></i>
      </div>
      <br>
      <div>
        <h4>{{ movie?.title }}</h4>
        <small>{{ movie?.production_countries_name }}</small>
        <h6>{{ movie?.director.name }}</h6>
      </div>
      <span v-for="genre in movie?.genres" :key="genre.id">
        <span class="badge text-bg-light" style="margin: 2%;">{{ genre.name }}</span>
      </span>
      <br>
      <br>
      <div>
        <div class="accordion" id="accordionExample">
          <div class="accordion-item">
            <h2 class="accordion-header" id="headingOne">
              <button class="accordion-button collapsed" style="background-color: #2c3e50; color: white;" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                <b>줄거리</b>
              </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse bg-dark" style="color: white;" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
              <div class="accordion-body">
                <p><small>{{ movie?.overview }}</small></p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-1"></div>
    <!-- 별점, 찜, 댓글 -->
    <div class="col-8 right">
      <div id="star-graph" style="padding: 5px 0px 5px;">
        <span style="display: flex; padding: 5px 0px 5px; justify-content: space-evenly;">
          <div>
            <ageBarView
            :movie="movie"/>
          </div>
          <div style="display: flex; align-items: center; margin-right:1%;">
            <!-- <genderBarView
            :movie="movie"/> -->
            <img :src="require('@/assets/female.png')" alt="" style="height: 50px; width:70px;">
            <p style="font-size: large; margin: 3%; margin-right: 20%;">{{ this.gender_average[0] }}</p>
            <img :src="require('@/assets/male.png')" alt="" style="height: 50px; width:70px;">
            <p style="font-size: large; margin: 3%; margin-right: 5%;">{{ this.gender_average[1] }}</p>
          </div>
        </span>
      </div>
      <br>
      <div id="star-jjim" style="margin: 1%;height: 15%;">
        <span class="col-5">
          <i class="fa-solid fa-star fa-3x" style="color: gold; margin:5%;"></i>
          <h5><b>{{ this.Star === 0 ? movie?.vote_average: this.Star }}</b></h5>
        </span>
        <span class="col-7" style="display: flex; justify-content: center; align-items: center; margin-left: 5%;">
          <select class="form-select form-select-sm" aria-label=".form-select-sm example" name="rate" v-model="MymovieRate" id="rate" style="height: 50%;">
            <option class="content-font" style="color:black;" :value="rate" v-for="(rate, idx) in this.$store.state.reviewRate" :key="idx">{{ rate }}</option>
          </select>
          <button v-if="this.$store.getters.isLogin === true" @click="starRate" type="button" class="btn btn-light" style="margin-left: 8%; height: 50%;">영화 평가하기</button>
          <button v-if="this.$store.getters.isLogin === false" type="button" class="btn btn-light" style="margin-left: 8%; height: 50%;" disabled>영화 평가하기</button>
          <br>
        </span>
      </div>
      <br>
      <hr>
      <br>
      <h3 style="color: yellow;">사용자 감상평</h3>
      <br>
      <div v-if="this.$store.getters.isLogin === true" id="comment-input" style="display: flex; align-items:center; margin: 1%; height: 15%;">
        <input class="form-control" style="width: 90%" type="text" placeholder="감상평을 공유해보세요!" aria-label="default input example" v-model.trim="content">
        <button @click="createComment" type="button" class="btn btn-light">입력</button>
      </div>
      <h5 v-if="this.$store.getters.isLogin === false">감상평을 남기려면 로그인하세요.</h5>
      <small v-if="this.$store.getters.isLogin === true" style="color: gray; margin-bottom: 3%;">{{ contentlength }} / 200</small>
      <div id="comment-box" style="height: 45%; margin: 1%; margin-left: 5%;">
        <MovieCommentsList
        v-for="comment of commentlist"
        :key="comment.pk"
        :comment="comment"
        />
      </div>
    </div>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
import axios from 'axios'
import MovieCommentsList from '@/views/Movies/MovieCommentsList'
import ageBarView from '@/views/Movies/ageBarView'

const API_URL = 'http://127.0.0.1:8000'

export default {
  
  name: 'DetailView',
  data() {
    return {
      movie: null,
      image_url: null,
      content: null,
      commentlist: null,
      MymovieRate: 0,
      Star: 0,
      gender_list: [0, 0],
      gender_count: [0, 0],
      gender_average: [0, 0],
      contentlength: 0,
    }
  },
  created() {
    this.getMovieDetail()
    this.getCommentDetail()
    this.plus()
  },
  watch: {
    content(newcontent) {
      if (newcontent.length > 200) {
        alert('감상평이 너무 깁니다.')
        this.username = newusername.slice(0, 200)
      }
      this.contentlength = newcontent.length
    }
  },
  components: { MovieCommentsList, ageBarView, },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/`
      })
      .then((res) => {
        this.movie = res.data
        let islike = false
        for (let i=0; i<res.data.like_users.length; i++) {
          if (res.data.like_users[i].id === this.$store.state.userid) {
            islike = true
          }
        }
        if (islike === true) {
          const heartTag = document.querySelector('#heart')
          heartTag.style.color = 'red'
        }
        this.image_url = `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ res.data.poster_path }`
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
        this.content = null
        this.contentlength = 0
      })
      .catch((err => {
        console.log(err)
      }))
    },
    getCommentDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/movie_comment/${this.$route.params.id}/`,
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
        this.$router.go({name: 'DetailView', params: { id: this.movie.id }})
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
    likes(event) {
      const tag = event.target
      if (tag.style.color === 'lightgray') {
        tag.style.color = 'crimson'
      } else {
        tag.style.color = 'lightgray'
      }
      if (this.$store.state.token != '') {
          axios({
            method: 'post',
            url: `${API_URL}/movies/${this.movie.id}/${this.$store.state.userid}/likes/`,
            headers: {
              "Authorization": `Token ${this.$store.state.token}`
            }
          })
            .then(res => {
              console.log(res)
            })
            .catch(err => {
              console.log(err)
            })
          }
    },
    plus() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/starinfo/`,
      })
      .then(res => {
          this.starlist = res.data
          axios({
          method: 'get',
          url: `${API_URL}/accounts-custom/usersinfo/`,
        })
        .then((res) => {
          this.userlist = res.data
          this.gender_list= [0, 0]
          this.gender_count = [0, 0],
          this.gender_average = [0, 0]
      for (var i = 0; i < this.starlist.length; i++) {
        for (var idx = 0; idx < this.userlist.length; idx++) {
          // console.log(i, idx)
          if (this.starlist[i]['user_id'] === this.userlist[idx]['id']) { 
            if (this.userlist[idx].sex === 'm') {
              this.gender_count[1] += 1
              this.gender_list[1] += this.starlist[i]['rank']
              this.gender_average[1] = (this.gender_list[1] / this.gender_count[1]).toFixed(2)
            } else if (this.userlist[idx].sex === 'f') {
              this.gender_count[0] += 1
              this.gender_list[0] += this.starlist[i]['rank']
              this.gender_average[0] = (this.gender_list[0] / this.gender_count[0]).toFixed(2)
              console.log(this.gender_average)
            }
            }
          }
        }
      })
    })
    }
  },
}
</script>

<style>
#detail {
  padding:5% 5% 5% 5%;
  height: 100vh;
}
.left {
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 4px;
  padding: 10px;
  float: left;
  width: 30%;
}
.right {
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 4px;
  padding: 10px;
  float: right;
  width: 70%;
}
#star-jjim {
  display : flex; 
  justify-content : space-around;
}

#rate {
  width: 70px;
}
</style>