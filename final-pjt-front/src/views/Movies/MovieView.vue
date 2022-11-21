<template>
  <div style="display: flex column; align-items: center;">
    <div v-if="LikesList[0].length" id="likeslist" style="margin: auto; margin-top: 2%;">
      <div>
        <br>
        <h4>내 팔로워 {{ usernames[0] }}님이 좋아해요</h4>
      </div>
      <div style="display: flex; justify-content: space-evenly;">
      <FollowerLikesList
      v-for="likemovie in LikesList[0]"
      :key="likemovie.id"
      :likemovie="likemovie"/>
      </div>
    </div>
    <div v-if="LikesList[1].length" id="likeslist" style="margin: auto; margin-top: 2%;">
      <div>
        <br>
        <h4>내 팔로워 {{ usernames[1] }}님이 좋아해요</h4>
      </div>
      <div style="display: flex; justify-content: space-evenly;">
      <FollowerLikesList
      v-for="likemovie in LikesList[1]"
      :key="likemovie.id"
      :likemovie="likemovie"/>
      </div>
    </div>
    <div v-if="LikesList[2].length" id="likeslist" style="margin: auto; margin-top: 2%;">
      <div>
        <br>
        <h4>내 팔로워 {{ usernames[2] }}님이 좋아해요</h4>
      </div>
      <div style="display: flex; justify-content: space-evenly;">
      <FollowerLikesList
      v-for="likemovie in LikesList[2]"
      :key="likemovie.id"
      :likemovie="likemovie"/>
      </div>
    </div>
    <br>
    <h3>최신 영화</h3>
    <div id="MovieView">
      <MovieCard v-for="(movie) in movies" :key="movie.id" :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieCard from '@/views/Movies/MovieCard.vue'
import FollowerLikesList from '@/views/Movies/FollowerLikesList.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'MovieView',
  components: {
    MovieCard,
    FollowerLikesList,
  },
  computed: {
    movies() { return this.$store.state.movies }
  },
  data() {
    return {
        LikesList: [[],[],[]],
        usernames: [],
    }
  },
  created() {
    this.movieget()
    this.followerOrRandom()
  },
  methods: {
    movieget() {
      this.$store.dispatch('movieGet')
    },
    followerOrRandom() {
      if (this.$store.state.token != '') {
        this.LikesList = [[],[],[]]
        axios({
            method: 'get',
            url: `${API_URL}/accounts-custom/${this.$store.state.userid}/followinfo/`,
            headers: {
                "Authorization": `Token ${this.$store.state.token}`
            }
        })
            .then(res => {
            if (res.data.followers.length) {
                let num = 1
                if (res.data.followers.length < 3) {
                    num = res.data.followers.length
                } else {
                    num = 3
                }
                for (let i=0; i<num; i++) {
                  this.usernames.push(res.data.followers[i].username)
                    axios({
                        method: 'get',
                        url: `${API_URL}/accounts-custom/${res.data.followers[i].id}/likeslist/`,
                        headers: {
                            "Authorization": `Token ${this.$store.state.token}`
                        }
                    })
                        .then(res => {
                            console.log(res)
                            let num = 0
                            if (res.data === '') {
                              this.LikesList[i] = []
                            } else if (res.data.length < 4) {
                              num = res.data.length
                            } else {
                              num = 4
                            }
                            for (let j=0; j<num; j++) {
                              this.LikesList[i].push(res.data[j])
                            }
                        })
                        .catch(err => {
                            console.log(err)
                        })
                }
            } else {
              console.log(0)
            }
            })
            .catch(err => {
            console.log(err)
            })
        }
    }
  }
}
</script>

<style>
#MovieView {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  height: 100%;
}
#likeslist {
  display: flex column;
  justify-content: center;
  width: 70%;
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: 4px;
  margin: 3%;
  flex-wrap: wrap;
}
</style>