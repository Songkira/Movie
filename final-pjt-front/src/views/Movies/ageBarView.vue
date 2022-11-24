<template>
  <div>
    <div style="height:100%; width:100%; margin: auto;">
      <Pie
        style="height:250px; width:250px;"
        :chart-options="chartOptions"
        :chart-data="chartData"
        :chart-id="chartId"
        :dataset-id-key="datasetIdKey"
        :plugins="plugins"
        :css-classes="cssClasses"
        :styles="styles"
        :width="width"
        :height="height"
      />
    </div>
  </div>
</template>


<script>
import 'chart.js/auto';
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ageBarView',
  components: { Pie },
  props: {
    chartId: {
      type: String,
      default: 'pie-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 400
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Array,
      default: () => []
    },
    movie: Object,
  },
  data() {
    return {
      chartData: {
        labels: [ '10대', '20대', '30대', '40대', '50대',  '60대 이상'],
        datasets: [ { data: [],
          backgroundColor: [
          'rgb(67, 215, 129)',
          'rgb(121, 220, 225)',
          'rgb(229, 119, 216)',
          'rgb(234, 182, 78)',
          'rgb(153, 102, 255)',
          'rgb(215, 229, 119)'
        ], } ],
      },
      chartOptions: {
        responsive: true,
      },
      movieslist: this.$store.state.movies,
      starlist : [],
      userlist: [],
      f_count: 0,
      m_count: 0,
      age_list: [0, 0, 0, 0, 0, 0],
      age_count: [0, 0, 0, 0, 0, 0],
      age_average: [0, 0, 0, 0, 0, 0],
      moviemovie: this.movie,
    }
  },
  computed: { },
  created() {
    // this.Starget()
    // this.userInfo()
    this.plus()
    this.charplus()
  },
  // watch: {
  //   moviemovie(newmovie) {
  //     console.log(newmovie)
  //     this.plus()
  //   }
  // },    
  methods: {
    // Starget() {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/movies/${this.$route.params.id}/starinfo/`,
    //   })
    //   .then(res => {
    //       this.starlist = res.data
    //   })
    //   .catch((err) => { console.log(err) })
    // },
    // userInfo() {
    //   axios({
    //       method: 'get',
    //       url: `${API_URL}/accounts-custom/usersinfo/`,
    //     })
    //     .then((res) => {
    //       this.userlist = res.data
    //     })
    //     .catch((err) => { console.log(err) })
    // },
    charplus() {
      this.chartData['datasets'][0]['data'] = this.age_average
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
          // console.log(this.age_list)
          this.f_count = 0
          this.m_count = 0
          this.age_list = [0, 0, 0, 0, 0, 0]
          this.age_count = [0, 0, 0, 0, 0, 0]
          this.age_average = [0, 0, 0, 0, 0, 0]
          for (var i = 0; i < this.starlist.length; i++) {
            for (var idx = 0; idx < this.userlist.length; idx++) {
              if (this.starlist[i]['user_id'] === this.userlist[idx]['id']) { 
                const birth = this.userlist[idx].birth.slice(0, 4)
                if ('2004' <= birth && birth < '2014') {
              this.age_count[0] += 1
              this.age_list[0] += this.starlist[i]['rank']
              this.age_average[0] =(this.age_list[0] / this.age_count[0]).toFixed(2)
              this.charplus()
            }
            else if ( '1994' <= birth && birth < '2004') {
              this.age_count[1] += 1
              this.age_list[1] += this.starlist[i]['rank']
              this.age_average[1] = (this.age_list[1] / this.age_count[1]).toFixed(2)
              this.charplus()
            }
            else if ('1984' <= birth && birth < '1994') {
              this.age_count[2] += 1
              this.age_list[2] += this.starlist[i]['rank']
              this.age_average[2] = (this.age_list[2] / this.age_count[2]).toFixed(2)
              this.charplus()
            } else if ('1974' <= birth && birth < '1984') {
              this.age_count[3] += 1
              this.age_list[3] += this.starlist[i]['rank']
              this.age_average[3] = (this.age_list[3] / this.age_count[3]).toFixed(2)
              this.charplus()
            } else if ('1964' <= birth && birth < '1974') {
              this.age_count[4] += 1
              this.age_list[4] += this.starlist[i]['rank']
              this.age_average[4] = (this.age_list[4] / this.age_count[4]).toFixed(2)
              this.charplus()
            } else if (birth < '1964') {
              this.age_count[5] += 1
              this.age_list[5] += this.starlist[i]['rank']
              this.age_average[5] = (this.age_list[5] / this.age_count[5]).toFixed(2)
              this.charplus()
            }
          }
        }
      }
    })
    })
    }
  }
}
</script>

<style>
#id {
  background-color: rgb(234, 182, 78);
}
</style>