<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input id="username" style="width:30%;" class="form-control" type="text" v-model.trim="username"><br>

      <label for="password1"> password : </label>
      <input id="password1" style="width:30%;" class="form-control" type="text" v-model.trim="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input id="password2" style="width:30%;" class="form-control" type="text" v-model.trim="password2"><br>
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      if (password1 === password2) {
        const payload = {
          username: username,
          password: password1,
        }
        this.$store.dispatch('signUp', payload)
      } else {
        alert('비밀번호와 비밀번호 확인이 다릅니다.')
      }
    }
  }
}
</script>

<style>
label {
  color: white;
}

</style>