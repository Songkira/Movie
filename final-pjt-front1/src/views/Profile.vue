<template>
  <div id="myprofile">
    <h2>닉네임: {{ person.personname }}</h2>
    <h2>팔로워/팔로우</h2>
    <button @click="followThis">Follow</button>
    <div>
        <h3>개인 설정</h3>
        <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
            <label class="form-check-label" for="flexSwitchCheckDefault">공포 장르 제외</label>
        </div>
        <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
            <label class="form-check-label" for="flexSwitchCheckDefault">19+ 제외</label>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'MyProfile',
  props: {
    person: Object,
  },
  data() {
    return {
      me: [],
      ps: this.person,
    }
  },
  methods: {
    followThis() {
      if (this.$store.state.token != '') {
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
            "Authorization": `Token ${this.$store.state.token}`
          }
        })
          .then(res => {
            this.me = res.data
            axios({
              method: 'post',
              url: `${API_URL}/accounts-custom/${res.data.pk}/${this.ps.pk}/follow/`,
            })
              .then(res => {
                console.log(res)
              })
              .catch(err => {
                console.log(err)
              })
          })
          .catch(err => {
            console.log(err)
          })
        }
      },
      getMyInfo() {
        if (this.$store.state.token != '') {
          axios({
            method: 'get',
            url: `${API_URL}/accounts/user/`,
            headers: {
            "Authorization": `Token ${this.$store.state.token}`
            }
          })
            .then(res => {
              console.log(res.data)
            })
            .catch(err => {
              console.log(err)
            })
          }
        },
    },
    
}

</script>

<style>
#myprofile {
    color: white;
}
</style>