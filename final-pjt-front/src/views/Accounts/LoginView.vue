<template>
  <div>
    <div class="card text-bg-dark" style="margin: 5%;">
      <!-- <img src="..." class="card-img" alt="..."> -->
      <div class="card-body" style="width:100%; height: 100%;">
        <br>
        <h1>LogIn</h1>
        <br>
        <form @submit.prevent="logIn">
          <div style="display: flex column; justify-content: center; align-items: center;">
            <div class="form-floating mb-3 col-7">
              <input type="text" class="form-control" id="username" v-model.trim="username" placeholder="닉네임 입력">
              <label for="username" style="color: gray;">닉네임</label>
            </div>
            <div class="form-floating col-7" style="margin-bottom: 5%;">
              <input type="password" class="form-control" id="password" v-model.trim="password" placeholder="비밀번호 입력">
              <label for="password" style="color: gray;">비밀번호</label>
            </div>
            <div style="margin-top: auto; margin-bottom: auto; margin-left: 1%;">
              <button type="submit" class="btn btn-light">로그인</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  created() {
    this.logOut()
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password
      const payload = {
        username: username, 
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    },
    logOut() {
      this.$store.dispatch('logOut')
    }
  }
} 
</script>

<style>
/* input::placeholder {
  color: gray !important;
} */
</style>