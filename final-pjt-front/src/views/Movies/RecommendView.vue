<template>
  <div id="recommend">
    <div style="width:10%">
      <p>추천 페이지</p>
      <select name="gnr" v-model="selectGenres" id="gnr">
        <option class="content-font" style="color:black;" :value="gnr" v-for="(gnr, idx) in this.$store.state.genrename" :key="idx">{{ gnr }}</option>
      </select>
      <select name="country" v-model="selectCountry" id="country">
        <option class="content-font" style="color:black;" :value="country" v-for="(country, idx) in this.countryname_list" :key="idx">{{ country }}</option>
      </select>
      <select name="year" v-model="selectYear" id="year">
        <option class="content-font" style="color:black;" :value="year" v-for="(year, idx) in yearname" :key="idx">{{ year }}</option>
      </select>
      <button @click="filterMovie">click</button>
    </div>
    <div style="width:90%">
      <RecommandListViewVue v-for="item in items" :key="item.id" :item="item" />
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
      selectGenres: null,
      selectCountry: null,
      selectYear: null,
      countryname_list: [],
    }
  },
  created() {
    this.stateGet()
    this.genreGet()
  },
  methods: {
    genreGet() {
      this.$store.dispatch('genreGet')
    },
    filterMovie() {
      this.items = []
      for (const movie of this.movies ) {
        const name = movie.production_countries_name
        const release_date = movie.release_date.slice(0,4)
        // console.log(release_date, typeof(release_date))
        for (const gen of movie.genres) {
          for (var i = 0; i < this.genrelist.length; i++) {
            for (var idx = 0; idx < this.countryname_list.length; idx++) {
              if (this.genrelist[i][1] === this.selectGenres && this.genrelist[i][0] === gen)  {
                if (this.countryname_list[idx] === this.selectCountry && this.countryname_list[idx] === name) {
                  if (this.selectYear === '90년대' && '1990' <= release_date && release_date < '2000'){
                    this.items.push(movie)
                    // console.log(release_date, typeof(release_date))
                  }
                  if (this.selectYear === '2000년대' && '2000' <= release_date && release_date < '2010') {
                    this.items.push(movie)
                    // console.log(release_date, typeof(release_date))
                  }
                  if (this.selectYear === '2010년대' && '2010' <= release_date && release_date < '2020'){
                    this.items.push(movie)
                    // console.log(release_date, typeof(release_date))
                  }
                  if (this.selectYear === '2020년대' && '2020' <= release_date){
                    this.items.push(movie)
                  }
                }
              }
            }
          }
        }
      }
    },
    stateGet() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/states/`,
      })
        .then((res) => {
          this.countrylist = res.data 
          // console.log(res.data[0]) for문 돌리기
          for (var i = 0; i < res.data.length; i++) {
            // if (!(res.data[i][1] in this.countryname_list)) {
            if (this.countryname_list.includes(res.data[i])) {
              continue
            } else {
              this.countryname_list.push(res.data[i])
            }
          }
        })
        .catch(err => console.log(err))
    }
  },
  computed: {
    genrelist() { return this.$store.state.genrelist },
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