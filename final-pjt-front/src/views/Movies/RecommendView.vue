<template>
  <div id="recommend">
    <div>
      <h3 class="m-3">{{ this.$store.state.username }}님께 추천해드릴게요!</h3>
      <div v-if="items.length === 0">
        <div style="height:550px;"></div>
      </div>
      <div v-if="items" style="display: flex; justify-content: space-evenly;">
        <RecommandListViewVue v-for="item in items" :key="item.id" :item="item" />
      </div>
      <div style="display: flex; justify-content: center;">
        <select class="form-select form-select-xs m-2" aria-label=".form-select-xs example" name="gnr" v-model="selectGenres" id="gnr">
          <option class="content-font" style="color:black;" value='전체' selected="selected">전체</option>
          <option class="content-font" style="color:black;" :value="gnr" v-for="(gnr, idx) in this.$store.state.genrename" :key="idx">{{ gnr }}</option>
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
      <button type="button" class="btn btn-light" @click="filterMovie">추천</button>
    </div>
  </div>
</template>

<script>
import RecommandListViewVue from '@/views/Movies/RecommandListView';

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
    }
  },
  created() {
    this.stateGet()
    this.genreGet()
    this.items = []
  },
  methods: {
    genreGet() {
      this.$store.dispatch('genreGet')
    },
    filterMovie() {
      this.items = []
      for (const movie of this.movies) {
        console.log(movie)
        const name = movie.production_countries_name
        const release_date = movie.release_date.slice(0,4)
        for (const gen of movie.genres) {
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
          break
        }
      }
      this.sortBy()
      this.items = this.items.slice(0, 3)
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
    // genrelist() { return this.$store.state.genrelist },
    movies() { return this.$store.state.movies },
    yearname() { return this.$store.state.yearname }
    
  }
}
</script>

<style>
  #recommend {
    height: 100vh;
  }
</style>