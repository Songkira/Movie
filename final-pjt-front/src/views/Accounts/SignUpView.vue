<template> 
  <div>
    <div class="card text-bg-dark" style="margin: 5%;">
      <!-- <img src="..." class="card-img" alt="..."> -->
      <div class="card-body" style="width:100%; height: 100%; display: flex column; justify-content: center;">
        <h1>회원가입</h1>
        <form class="col-7" style="margin: auto;" @submit.prevent="signUp">
          <div class="form-floating mb-3">
            <input type="text" class="form-control" id="username" v-model.trim="username" placeholder="닉네임">
            <label for="username" style="color: gray;">닉네임</label>
          </div>

          <div class="form-floating mb-3">
            <input type="password" class="form-control" id="password1" v-model.trim="password1" placeholder="비밀번호">
            <label for="password1" style="color: gray;">비밀번호</label>
          </div>

          <div class="form-floating" style="margin-bottom: 5%;">
            <input type="password" class="form-control" id="password2" v-model.trim="password2" placeholder="비밀번호 확인">
            <label for="password2" style="color: gray;">비밀번호 확인</label>
          </div>

          <div class="form-check col-3">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" v-model.trim="male">
            <label class="form-check-label" for="flexRadioDefault1">
              남자
            </label>
          </div>
          <div class="form-check col-3">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked v-model.trim="female">
            <label class="form-check-label" for="flexRadioDefault2">
              여자
            </label>
          </div>
          <br>
          <div>
            <h5 for="example-datepicker">생년월일</h5>
            <b-form-datepicker id="example-datepicker" v-model="date" class="mb-2"></b-form-datepicker>
          </div>
          <br>
          <button type="submit" class="btn btn-light">등록</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>

          // :picker-options="startDateOptions" 
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      male: false,
      female: false,
      date: '2000-01-01'
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const date = this.date
      console.log(this.male)
      console.log(this.female)
      if (password1 === password2) {
        let sex = null
        if (this.male === null) {
          sex = 'f'
        } else if (this.female === null) {
          sex = 'm'
        }
        const payload = {
          username: username,
          password: password1,
          sex: sex,
          birth: date,
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