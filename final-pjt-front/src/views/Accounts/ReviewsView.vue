<template>
  <div>
    <button type="button" class="btn btn-light m-2" data-bs-toggle="modal" data-bs-target="#reviewcreate">영화 카드 추가</button>
    <div style="display: flex; justify-content: center;">
      <div id="reviews" class="col-6">
        <ReviewsList/>
      </div>
    </div>
    <!-- Modal -->
    <div class="modal fade" id="reviewcreate" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" style="color: black;" id="exampleModalLabel">영화 감상 카드 만들기</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="close"></button>
          </div>
          <div class="modal-body" @submit.prevent="searchMovie">
            <form class="d-flex" role="search">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model.trim="searchword" @keyup="wordchange">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
            <div style="display: flex; flex-wrap: wrap;">
              <SearchResults
              v-for="movie in results"
              :key="movie.id"
              :movie="movie"
              @selectmv="selectmv"
              data-bs-dismiss="modal" aria-label="Close"
              />
            </div>
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
      selectmovie: {}
    }
  },
  created() {
    this.getReviews
  },
  watch: {
    selectmovie() {}
  },
  methods: {
    getReviews() {
      axios({
      method: 'get',
        url: `${API_URL}/movies/${this.movie.id}/${this.$store.state.userid}/reviews/`,
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
    },
    wordchange(event) {
      this.searchword = event.target.value
      this.searchMovie()
    },
    close() {
      this.searchword = ''
      this.results = []
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
    }
  }
}
</script>

<style>
#reviews {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  padding: 5%;
}
</style>