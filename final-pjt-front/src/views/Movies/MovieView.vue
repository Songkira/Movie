<template>
  <div style="display: flex column; align-items: center;">
    <div v-if="LikesList[0].length" id="likeslist" class="col-10" style="margin: auto; margin-top: 2%;">
      <div>
        <br>
        <h4>내 친구 <b @click="personPageGo" @mouseenter="selectCard" @mouseleave="selectCard">{{ usernames[0] }}</b>님이 좋아해요</h4>
      </div>
      <div style="display: flex; justify-content: center;">
      <FollowerLikesList
      v-for="likemovie in LikesList[0]"
      :key="likemovie.id"
      :likemovie="likemovie"/>
      </div>
    </div>
    <div v-if="LikesList[1].length" id="likeslist" class="col-10" style="margin: auto; margin-top: 2%;">
      <div>
        <br>
        <h4>내 친구 <b @click="personPageGo" @mouseenter="selectCard" @mouseleave="selectCard">{{ usernames[1] }}</b>님이 좋아해요</h4>
      </div>
      <div style="display: flex; justify-content: center;">
      <FollowerLikesList
      v-for="likemovie in LikesList[1]"
      :key="likemovie.id"
      :likemovie="likemovie"/>
      </div>
    </div>
    <div v-if="LikesList[2].length" id="likeslist" class="col-10" style="margin: auto; margin-top: 2%;">
      <div>
        <br>
        <h4>내 친구 <b @click="personPageGo" @mouseenter="selectCard" @mouseleave="selectCard">{{ usernames[2] }}</b>님이 좋아해요</h4>
      </div>
      <div style="display: flex; justify-content: center;">
      <FollowerLikesList
      v-for="likemovie in LikesList[2]"
      :key="likemovie.id"
      :likemovie="likemovie"/>
      </div>
    </div>
    <br>
    <div style="position: absolute; margin: auto;">
      <div style="position: absolute; display: flex; margin-left: 70%;">
        <select  class="form-select" aria-label="Default select example" name="sort" v-model="selectSort" id="sort" style="height:1%;">
          <option class="content-font" style="color:black;" :value="sort" v-for="(sort, idx) in this.sortList" :key="idx">{{ sort }}</option>
        </select>
        <button type="button" class="btn btn-light" @click="SortBy">Go</button>
      </div>
      <h3>최신 영화</h3>
      <div id="MovieView" class="col-10" style="margin: auto;">
        <MovieCard v-for="(movie) in movieslist" :key="movie.id" :movie="movie"
        />
      </div>
    </div>
    <div style="position:fixed; top:85%; right:0%">
        <img :src="require(`@/assets/cat.png`)" alt="cinema_img" style="height: 100px; width: 100px;">
    </div>
  </div>
</template>

<script>
import MovieCard from '@/views/Movies/MovieCard.vue'
import FollowerLikesList from '@/views/Movies/FollowerLikesList.vue'
import axios from 'axios'
import _ from 'lodash'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'MovieView',
  components: {
    MovieCard,
    FollowerLikesList,
  },
  computed: {
    // movies() { return this.$store.state.movies }
  },
  data() {
    return {
        LikesList: [[],[],[]],
        usernames: [],
        selectSort: null,
        sortList: ['랜덤순', '인기도순', '평점순', '러닝타임순'],
        movieslist: this.$store.state.movies,
    }
  },
  created() {
    this.movieget()
    this.follower()
  },
  methods: {
    movieget() {
      this.$store.dispatch('movieGet')
    },
    follower() {
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
            if (res.data.followings.length) {
                let num = 1
                if (res.data.followings.length < 3) {
                    num = res.data.followings.length
                } else {
                    num = 3
                }
                for (let i=0; i<num; i++) {
                  this.usernames.push(res.data.followings[i].username)
                    axios({
                        method: 'get',
                        url: `${API_URL}/accounts-custom/${res.data.followings[i].id}/likeslist/`,
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
    },
    SortBy() {
      if (this.selectSort === '랜덤순') {
        this.movieslist = _.shuffle(this.$store.state.movies)
        // this.movieslist = this.movieslist.slice(0, 20)
        console.log(this.movieslist)
      }
      if (this.selectSort === '인기도순') {
        this.movieslist = this.$store.state.movies
        this.Popularity()
        // this.movies.slice(20)
        console.log(this.movieslist)
      }
      if (this.selectSort === '평점순') {
        this.movieslist = this.$store.state.movies
        this.Vote()
        // this.movies.slice(20)
        console.log(this.movieslist)
      }
      if (this.selectSort === '러닝타임순') {
        this.movieslist = this.$store.state.movies
        this.Runtime()
        // this.movies.slice(20)
        console.log(this.movieslist)
      }
    },
    Popularity() {
      this.movieslist.sort(function(a, b) {
        return b.popularity - a.popularity
      })
      // this.movieslist = this.movieslist.slice(0, 20)
    },
    Vote() {
      this.movieslist.sort(function(a, b) {
        return b.vote_average - a.vote_average        
      })
      // this.movieslist = this.movieslist.slice(0, 20)
    },
    Runtime() {
      const movieslistruntime = []
      for (let i=0; i<this.movieslist.length; i++) {
        if (this.movieslist[i].runtime !== 0) {
          movieslistruntime.push(this.movieslist[i])
        }
      }
      this.movieslist = movieslistruntime
      this.movieslist.sort(function(a, b) {
        return a.runtime - b.runtime
      })
      // this.movieslist = this.movieslist.slice(0, 20)
    },
    personPageGo(event) {
      this.$router.push({ name:"MyPage", params: { personname: event.target.innerText } })
    },
    selectCard(event) {
      const card_index = event.target
      if (card_index.style.color === 'pink') {
        card_index.style.color = 'white'
      } else {
        card_index.style.color = 'pink'
      }
    },
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