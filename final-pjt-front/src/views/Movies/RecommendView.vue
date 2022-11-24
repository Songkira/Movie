<template>
  <div id="recommend">
    <div>
      <br>
      <br>
      <h3 class="m-3 animate__animated animate__bounce" style=" margin-bottom: 0px;">{{ this.$store.state.username }}님께 추천해드릴게요!</h3>
      <div style="display: flex; justify-content: space-evenly;">
        <select class="form-select form-select-xs m-2" aria-label=".form-select-xs example" name="gnr" v-model="selectGenres" id="gnr">
          <option class="content-font" style="color:black;" value='전체' selected="selected">전체</option>
          <option class="content-font" style="color:black;" :value="gnr" v-for="(gnr, idx) in this.genrename" :key="idx">{{ gnr }}</option>
        </select>
        <select class="form-select form-select-xs m-2" aria-label=".form-select-xs example" name="country" v-model="selectCountry" id="country">
          <option class="content-font" style="color:black;" value='전체' selected="selected">전체</option>
          <option class="content-font" style="color:black;" :value="country" v-for="(country, idx) in this.countryname_list" :key="idx">{{ country }}</option>
        </select>
        <select class="form-select form-select-xs m-2" aria-label=".form-select-xs example" name="year" v-model="selectYear" id="year">
          <option class="content-font" style="color:black;" value='전체' selected="selected">전체</option>
          <option class="content-font" style="color:black;" :value="year" v-for="(year, idx) in this.yearname" :key="idx">{{ year }}</option>
        </select>
      </div>
      <br>
      <button type="button" class="btn btn-light col-3" @click="filterMovie">추천 받기!</button>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <div v-if="items.length === 0" >
        <div style="display: flex; justify-content: center; margin-top: 10%; height:600px;">
          <h5 v-if="iszero">{{ this.$store.state.username }}님이 원하는 조건의 영화가 없습니다...</h5>
        </div>
      </div>
      <div v-if="items" style="display: flex; justify-content: center; " >
        <RecommandListViewVue style="height:600px;" class="animate__animated animate__flipInY" v-for="(item, idx) in items" :key="item.id" :item="item" :idx="idx"/>
      </div>
    </div>
  </div>
</template>

<script>
import RecommandListViewVue from '@/views/Movies/RecommandListView';

import 'animate.css'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'RecommendView',
  components: { RecommandListViewVue },
  data() {
    return  {
      items: [],
      selectGenres: '전체',
      selectCountry: '전체',
      selectYear: '전체',
      countryname_list: [],
      yearname: [ '80년대', '90년대', '2000년대', '2010년대', '2020년대'],
      genrename: [
      "액션","모험","애니메이션","코미디","범죄","다큐멘터리","드라마","가족","판타지",
      "역사","공포","음악","미스터리","로맨스","SF","TV 영화","스릴러","전쟁","서부"],
      iszero: false,
    }
  },
  created() {
    this.stateGet()
    // this.genreGet()
    this.items = []
  },
  methods: {
    // genreGet() {
    //   this.$store.dispatch('genreGet')
    // },
    filterMovie() {
      this.items = []
      for (const movie of this.movies) {
        // console.log(movie)
        const name = movie.production_countries_name
        const release_date = movie.release_date.slice(0,4)
        for (const gen of movie.genres) {
          console.log(gen.name)
          if (gen.name === this.selectGenres || this.selectGenres === '전체') {
            if (name === this.selectCountry || this.selectCountry === '전체') {
              if (this.selectYear === '전체') {
                this.items.push(movie)
              }
              if (this.selectYear === '80년대' && '1980' <= release_date && release_date < '1990'){
                this.items.push(movie)
              }
              if (this.selectYear === '90년대' && '1990' <= release_date && release_date < '2000'){
                this.items.push(movie)
              }
              if (this.selectYear === '2000년대' && '2000' <= release_date && release_date < '2010') {
                this.items.push(movie)
              }
              if (this.selectYear === '2010년대' && '2010' <= release_date && release_date < '2020'){
                this.items.push(movie)
              }
              if (this.selectYear === '2020년대' && '2020' <= release_date){
                this.items.push(movie)
              }
            }
          }
          if (this.items.includes(movie)) {
            break
          }
        }
      }
      this.sortBy()
      this.items = this.items.slice(0, 3)
      if (this.items.length === 0) {
        this.iszero = true
      } else {
        this.iszero = false
      }
    },
    stateGet() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/states/`,
      })
        .then((res) => {
          this.countrylist = res.data
          for (var i = 0; i < res.data.length; i++) {
            if (this.countryname_list.includes(res.data[i])) {
              continue
            } else if (res.data[i] !== '') {
              this.countryname_list.push(res.data[i])
            }
          }
        })
        .catch(err => console.log(err))
    },
    sortBy() {
      this.items.sort(function(a, b) {
        return b.popularity - a.popularity
      })
    },
  },
  computed: {
    movies() { return this.$store.state.movies },
  }
}
</script>

<style>
  #recommend {
    height: 100vh;
  }
  :root {
    --animate-delay: 2s;
  }
</style>