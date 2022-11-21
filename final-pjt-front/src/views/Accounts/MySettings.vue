<template>
  <div id="mysettings" class="col-8" style="display: flex; justify-content: center; margin: auto; margin-top: 5%;">
    <br>
    <div class="col-6" style="margin:5%;">
        <h3>개인 설정</h3>
        <br>
        <br>
        <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" v-model="nofear">
            <label class="form-check-label" for="flexSwitchCheckDefault"><b>공포 제외</b></label>
        </div>
        <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" v-model="nothrill">
            <label class="form-check-label" for="flexSwitchCheckDefault"><b>스릴러 제외</b></label>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'MySettings',
  data() {
    return {    
      nofear: this.$store.state.usernofear,
      nothrill: this.$store.state.usernothrill,
    }
  },
  created() {
    console.log(this.$store.state.usernofear)
    console.log(this.$store.state.usernothrill)
  },
  watch: {
    nofear (nofear) {
      console.log(nofear)
      let result = 'F'
      if (nofear === false) {
        result = 'F'
      } else {
        result = 'T'
      }
      axios({
        method: 'put',
        url: `${API_URL}/accounts-custom/${this.$store.state.userid}/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`
          },
        data: {
          "username": this.$store.state.username,
          "password": this.$store.state.password,
          "sex": this.$store.state.usersex,
          "nofear": result
        }
      })
        .then(res => {
            console.log(res)
            this.$store.dispatch('changeSettings')
        })
        .catch(err => {
            console.log(err)
        })
    },
    nothrill (nothrill) {
      console.log(nothrill)
      let result = 'F'
      if (nothrill === false) {
        result = 'F'
      } else {
        result = 'T'
      }
      axios({
        method: 'put',
        url: `${API_URL}/accounts-custom/${this.$store.state.userid}/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`
          },
        data: {
          "username": this.$store.state.username,
          "password": this.$store.state.password,
          "sex": this.$store.state.usersex,
          "nothrill": result
        }
      })
        .then(res => {
            console.log(res)
            this.$store.dispatch('changeSettings')
        })
        .catch(err => {
            console.log(err)
        })
    }
  },
}
</script>

<style>

</style>