<template>
  <div>
    <br>
    <h3>나의 포토티켓 기록</h3>
    <button type="button" class="btn btn-light m-2" data-bs-toggle="modal" data-bs-target="#reviewcreate">포토티켓 추가</button>
    <div style="display: flex; justify-content: center;">
      <div v-if="reviews.length !== 0" id="reviews" class="col-8">
        <ReviewsList
        v-for="review in this.reviews"
        :key="review.id"
        :review="review"/>
      </div>
    </div>
    <!-- Modal -->
    <div class="modal fade" id="reviewcreate" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" style="color: black;" id="exampleModalLabel">영화 포토티켓 만들기</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="close"></button>
          </div>
          <div class="modal-body" @submit.prevent="searchMovie">
            <form v-if="this.selectmovie.length === 0" class="d-flex" role="search">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model.trim="searchword" @keyup="wordchange">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
            <div v-if="this.selectmovie.length === 0" style="display: flex; flex-wrap: wrap;">
              <SearchResults
              v-for="movie in results"
              :key="movie.id"
              :movie="movie"
              @selectmv="selectmv"
              />
            </div>
            <form v-if="this.selectmovie.length !== 0" @submit.prevent="createReview">
              <span style="display: flex; margin: 0%;">
                <span class="card text-bg-dark col-5" style="width: 150px; margin: 0.5%;">
                  <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.selectmovie?.poster_path }`" class="card-img" alt="..." style="width: 150px;">
                  <!-- <div class="card-img-overlay" style="width:150px;">
                  </div> -->
                </span>
                <span class="col-7" style="justify-content: center;">
                  <h5 class="card-title" style="color: black;">{{ selectmovie.title }}</h5>
                </span>
              </span>
              <div>
                <h5 for="example-datepicker">영화를 본 날짜</h5>
                <b-form-datepicker id="example-datepicker" v-model="createdate" class="mb-2"></b-form-datepicker>
              </div>
              <div class="form-floating">
                <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea" v-model.trim="createtitle"></textarea>
                <label for="floatingTextarea" style="color: black;">제목</label>
              </div>
              <small style="color: gray;">{{ titlelength }} / 100</small>
              <div class="form-floating">
                <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 200px" v-model.trim="createcontent"></textarea>
                <label for="floatingTextarea2" style="color: black;">내용</label>
              </div>
              <small style="color: gray; margin-bottom: 3%;">{{ contentlength }} / 300</small>
              <br>
              <br>
              <button class="btn btn-outline-success" type="submit" data-bs-dismiss="modal" aria-label="Close">입력</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewsList from '@/views/Accounts/ReviewsList.vue'
import SearchResults from  '@/views/Accounts/SearchResults.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ReviewsView',
  components: {
    ReviewsList,
    SearchResults,
  },
  data() {
    return {
      reviews: [],
      results: [],
      searchword: '',
      selectmovie: '',
      createtitle: '',
      createcontent: '',
      createdate: '2022-01-01',
      titlelength: 0,
      contentlength: 0,
    }
  },
  created() {
    this.getReviews()
  },
  watch: {
    createtitle(newtitle) {
      if (newtitle.length > 100) {
        alert('제목이 너무 깁니다.')
        this.createtitle = newtitle.slice(0, 100)
      }
      this.titlelength = newtitle.length
    },
    createcontent(newcontent) {
      if (newcontent.length > 300) {
        alert('내용이 너무 깁니다.')
        this.createcontent = newcontent.slice(0, 300)
      }
      this.contentlength = newcontent.length
    },
  },
  methods: {
    getReviews() {
      axios({
      method: 'get',
        url: `${API_URL}/movies/${this.$store.state.userid}/reviews/`,
        headers: {
            "Authorization": `Token ${this.$store.state.token}`
          } 
    })
      .then(res => {
        this.reviews = res.data
        this.SortDate()
      })
      .catch(err => {
        console.log(err)
      })
    },
    wordchange(event) {
      this.searchword = event.target.value
      this.searchMovie()
    },
    close() {
      this.searchword = ''
      this.results = []
      // this.searchMovie = {}
      this.selectmovie = ''
      this.createtitle = ''
      this.createcontent = ''
      this.createdate = '2022-01-01'
      this.titlelength = 0
      this.contentlength = 0
    },
    searchMovie() {
      if (this.searchword.length !== 0) {
        const word = this.searchword
        const base = this.$store.state.movies
        const rst = []
        for (let i=0; i<base.length; i++) {
          if (base[i].title.includes(word)) {
            rst.push(base[i])
          } else if (base[i].overview.includes(word)) {
            rst.push(base[i])
          }
        }
        this.results = rst
      } else {
        this.results = []
      }
    },
    selectmv(sltmovie) {
      this.selectmovie = sltmovie
      console.log(this.selectmovie)
    },
    createReview() {
      axios({
      method: 'post',
        url: `${API_URL}/movies/${this.selectmovie.id}/${this.$store.state.userid}/reviews/`,
        headers: {
            "Authorization": `Token ${this.$store.state.token}`
        },
        data: {
          'movie': this.selectmovie.id,
          'user': this.$store.state.userid,
          'title': this.createtitle,
          'content': this.createcontent,
          'watch_date': this.createdate
        }
    })
      .then(() => {
        this.close()
        this.$router.go({name: 'ReviewsView', params:{'username': this.$store.state.username}})
      })
      .catch(err => {
        console.log(err)
      })
    },
    SortDate() {
      this.reviews.sort(function(a, b) {
        return new Date(b.watch_date) - new Date(a.watch_date)
      })
    }
  }
}
</script>

<style>
#reviews {
  display: flex;
  justify-content: space-evenly;
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: 4px;
  padding: 5%;
  flex-wrap: wrap;
}
</style>