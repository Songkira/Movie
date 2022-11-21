<template>
  <div style="display: flex; justify-content: center;">
    <span class="col-4" style="width: 300px; margin-top: 4%;">
        <br>
        <br>
        <Profile/>
    </span>
    <span style="width: 100px;">
    </span>
    <span class="col-8">
        <br>
        <br>
        <MyList/>
    </span>
    <p></p>
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'
// const personname = 'test1'

import Profile from '@/views/Accounts/Profile.vue'
import MyList from '@/views/Accounts/MyList.vue'
export default {
    name: 'MyPageView',
    data() {
      return {
        person: {},
      }
    },
    components: {
      Profile,
      MyList
    }
}
</script>

<style>

</style>