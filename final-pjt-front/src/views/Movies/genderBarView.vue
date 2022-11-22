<template>
  <div>
    <div style="height:100%; width:50%;">
      <Bar
        style="width:200px;"
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
    <!-- <button @click="plus">+</button> -->
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
import 'chart.js/auto';
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'genderBarView',
  components: { Bar },
  props: {
    chartId: {
      type: String,
      default: 'bar-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 100
    },
    height: {
      type: Number,
      default: 100
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
        labels: [ '여자', '남자' ],
        datasets: [ { data: [],
          backgroundColor: [
          'rgb(153, 102, 255)',
          'rgb(255, 159, 64)'
        ],
          label: '성별' ,
          borderWidth: 1
        } ],
      },
      chartOptions: {
        responsive: false,
        defaultFontColor: "rgb(255, 159, 64)",
        legend: {
          labels: {
            fontColor: "rgb(255, 159, 64)"
            // fontSize
          },
        },
        // scales: {
        //   y: {
        //     ticks: {
        //       // beginAtZero: true,
        //       // min: 0,
        //       // max: 100,
        //       // stepSize : 5,
        //       // suggestedMax: 100
        //       // fontSize : 14,
        //     }
        //   }
        // },
      },
      
      movieslist: this.$store.state.movies,
      starlist : [],
      userlist: [],
      f_count: 0,
      m_count: 0,
      age_list: [0, 0, 0, 0, 0, 0]
    }
  },
  computed: { },
  created() {
    this.plus()
    this.charplus()
  },
  methods: {
    charplus() {
      this.chartData['datasets'][0]['data'] = [ this.f_count , this.m_count ]
    },
    plus() {
      this.f_count = 0
      this.m_count = 0
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
      for (var i = 0; i < this.starlist.length; i++) {
        for (var idx = 0; idx < this.userlist.length; idx++) {
          // console.log(i, idx)
          if (this.starlist[i]['user_id'] === this.userlist[idx]['id']) { 
            if (this.userlist[idx].sex === 'm') {
              this.m_count += 1
              this.charplus()
            } else if (this.userlist[idx].sex === 'f') {
              this.f_count += 1
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

</style>