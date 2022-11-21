<template>
  <div>
    <h1>내가 찜한 영화</h1>
    <div id="likemovie">
      <MyMoviesList
      v-for="(movie, idx) in likeMovies"
      :key="movie.id"
      :movie="movie"
      @nolike="nolike(idx)"/>
    </div>
    <br>
      <h1>나의 평가</h1>
    <div id="mycomments">
      <MyCommentsList
      v-for="(comment, idx) in myComments"
      :key="idx"
      :comment="comment"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
import MyMoviesList from '@/views/Accounts/MyMoviesList.vue'
import MyCommentsList from '@/views/Accounts/MyCommentsList.vue'
export default {
    name: 'MyList',
    components: {
        MyMoviesList,
        MyCommentsList,
    },
    data() {
      return {
        personname: this.$route.params.personname,
        person: {},
        likeMovies: [],
        myComments: [],
      }
    },
    created() {
      axios({
          method: 'get',
          url: `${API_URL}/accounts-custom/usersinfo/`,
          headers: {
            "Authorization": `Token ${this.$store.state.token}`
            }
        })
          .then(res => {
            const prmts = { pk: -1, personname: null }
            for (let i=0; i < res.data.length; i++) {
              if (res.data[i].username === this.personname) {
                prmts.pk = res.data[i].id
                prmts.personname = res.data[i].username
                break
              }
            }
            console.log(prmts)
            this.person = prmts
            this.getLikeMovies()
            this.getMyComments()
          })
          .catch(err => {
            console.log(err)
          })
    },
    methods: {
      getLikeMovies() {
        axios({
          method: 'get',
          url: `${API_URL}/movies/${this.person.pk}/likemovies/`,
          headers: {
            "Authorization": `Token ${this.$store.state.token}`
            }
          })
            .then(res => {
              this.likeMovies = res.data
              console.log('****')
              console.log(this.likeMovies)
            })
            .catch(err => {
              console.log(err)
            })
          
      },
      getMyComments() {
        axios({
            method: 'get',
            url: `${API_URL}/movies/${this.person.pk}/mycomments/`,
            headers: {
                "Authorization": `Token ${this.$store.state.token}`
                }
            })
                .then(res => {
                  this.myComments = res.data
                })
                .catch(err => {
                    console.log(err)
                })
        },
        nolike() {
          this.getLikeMovies()
        }

    }
}
</script>

<style>
#likemovie {
  display: flex;
  justify-content: space-evenly;
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: 4px;
  padding: 5%;
  flex-wrap: wrap;
}

#mycomments {
  display: flex column;
  justify-content: center;
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: 4px;
  padding: 5%;
}
</style>