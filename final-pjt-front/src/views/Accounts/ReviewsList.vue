<template>
  <span class="card text-bg-light" style="position: relative; margin: 0.5%; padding: 1.5%; padding-bottom: 0%;">
    <img :src="image_url" class="card-img" alt="..." style="width: 150px;">
    <div class="card-img-overlay" style="width:150px;" type="button" data-bs-toggle="modal" :data-bs-target="`#reviewread${review.id}`">
      <i @click="reviewdelete" class="fa-regular fa-circle-xmark fa-xl" style="position: absolute; bottom: 6%; right: -9%;"></i>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
    </div>
    <h6 class="card-title" style="margin-top: 5%; width:150px;"><small>{{ review.watch_date }}</small></h6>
    <!-- Modal -->
    <div class="modal fade" :id="`reviewread${review.id}`" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" style="color: black;" id="exampleModalLabel">나의 영화 포토 일기</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body" @submit.prevent="searchMovie">
            <span style="display: flex; margin: 0%;">
              <span class="card text-bg-dark col-5" style="width: 150px; margin: 0.5%;">
                <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ review.movieinfo.poster_path }`" class="card-img" alt="..." style="width: 150px;">
                <!-- <div class="card-img-overlay" style="width:150px;">
                </div> -->
              </span>
              <span class="col-7" style="justify-content: center;">
                <h5 class="card-title" style="color: black;">{{ review.movieinfo.title }}</h5>
                <br>
                <br>
                <br>
                <h6 style="color: black;">{{ review.watch_date }}</h6>
              </span>
            </span>
            <div class="form-floating">
              <textarea class="form-control" type="text" :value="review.title" aria-label="readonly input example" id="floattitle" readonly></textarea>
              <label for="floattitle" style="color: black;">제목</label>
            </div>
            <div class="form-floating">
              <textarea class="form-control" type="text" :value="review.content" aria-label="readonly input example" id="floatcontent" style="height: 200px; overflow: visible; white-space: normal; word-wrap: break-word;" readonly></textarea>
              <label for="floatcontent" style="color: black;">내용</label>
            </div>
          </div>
        </div>
      </div>
    </div>
  </span>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ReviewsList',
  props: {
    review: Object,
  },
  created() {
    console.log('durl')
    console.log(this.review)
  },
  data() {
    return {
      image_url: `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${ this.review.movieinfo.poster_path }`
    }
  },
  methods: {
    detailGo() {
      this.$router.push({ name:"DetailView", params: { id: this.movie.id } })
    },
    reviewdelete() {
      console.log(this.movie)
      axios({
        method: 'delete',
        url: `${API_URL}/movies/${this.review.movieinfo.id}/${this.$store.state.userid}/reviews/`,
        headers: {
            "Authorization": `Token ${this.$store.state.token}`
        },
        data: {
          'reviewid': this.review.id
        }
      })
        .then(() => {
          this.$router.go({name: 'ReviewsView', params:{'username': this.$store.state.username}})
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
}
</script>

<style>

</style>