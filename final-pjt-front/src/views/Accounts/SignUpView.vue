<template> 
  <div style="display: flex; justify-content: center;">
    <div class="card text-bg-light col-8" style="margin: 5%;">
      <div class="card-body" style="width:100%; height: 100%; display: flex column; justify-content: center; background-color: rgb(0, 0, 0, 0.01);">
        <h1>회원가입</h1>
        <form class="col-8" style="margin: auto;" @submit.prevent="signUp">
          <br>
          <div>
            <h5>나의 고양이 사진</h5>
            <div v-if="!randomnumber" id="personimg" style="display: flex; justify-content: center; align-items: center; width: 130px; height: 130px; margin: auto;">
              <i class="fa-solid fa-paw fa-3x"></i>
            </div>
            <img v-if="randomnumber" :src="require(`@/assets/catpic/cat_ (${randomnumber}).jpg`)" alt="" id="personimg" style="width:130px; margin-bottom: 8%;">
            <br>
            <button type="button" class="btn btn-warning animate__animated animate__headShake mb-3" @click="catpick">야옹아 이리온</button>
          </div>
          <div class="form-floating mb-3" style="display:flex;">
            <input type="text" class="form-control" id="username" v-model.trim="username" placeholder="닉네임">
            <label for="username" style="color: gray;">닉네임</label>
            <button type="button" class="btn btn-secondary col-3" @click="isdupli">중복 확인</button>
          </div>
          <small class="mb-2" v-show="this.namedupli" style="color: gray;">사용할 수 있는 닉네임입니다.</small>
          <div class="form-floating mb-3">
            <input type="password" class="form-control" id="password1" v-model.trim="password1" placeholder="비밀번호">
            <label for="password1" style="color: gray;">비밀번호</label>
          </div>

          <div class="form-floating" style="margin-bottom: 2%;">
            <input type="password" class="form-control" id="password2" v-model.trim="password2" placeholder="비밀번호 확인" @keyup="checkpassword">
            <label for="password2" style="color: gray;">비밀번호 확인</label>
          </div>
          <small class="mb-2" v-show="!passwordsame && password2 !== ''" style="color: gray;">비밀번호가 동일하지 않습니다.</small>

          <div>
            <h5 for="example-datepicker">생년월일</h5>
            <b-form-datepicker id="example-datepicker" v-model="date" class="mb-2"></b-form-datepicker>
          </div>
          <br>

          <div class="form-check col-3">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1" value="m" @click="maleorfemale">
            <label class="form-check-label" for="flexRadioDefault1" style="color: black;">
              남자
            </label>
          </div>
          <div class="form-check col-3">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" value="f" @click="maleorfemale">
            <label class="form-check-label" for="flexRadioDefault2" style="color: black;">
              여자
            </label>
          </div>
          <br>
          <br>
          <button type="submit" class="btn btn-secondary">등록</button>
        </form>
        <br>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: '',
      sex: '',
      date: '2000-01-01',
      namedupli: false,
      passwordsame: '',
      randomnumber: 0,
    }
  },
  watch: {
    username(newusername) {
      if (newusername.length > 150) {
        alert('닉네임이 너무 깁니다.')
        this.username = newusername.slice(0, 150)
      }
    },
    password1(newpassword) {
      if (newpassword.length > 150) {
        alert('비밀번호가 너무 깁니다.')
        this.password1 = newpassword.slice(0, 150)
      }
    },
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const date = this.date
      const sex = this.sex
      if (this.namedupli === true) {
        if (password1 === password2) {
          const payload = {
            username: username,
            password: password1,
            sex: sex,
            birth: date,
            catpic: this.randomnumber
          }
          this.$store.dispatch('signUp', payload)
        } else {
          alert('비밀번호와 비밀번호 확인이 다릅니다.')
        }
      } else {
        alert('중복된 닉네임인지 확인해주세요.')
      }
    },
    maleorfemale(event) {
      this.sex = event.target.value
      console.log(this.sex)
    },
    isdupli() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts-custom/usersinfo/`,
      })
        .then(res => {
          let dupli = true
          for (let i=0; i<res.data.length; i++) {
            if (res.data[i].username === this.username) {
              this.namedupli = false
              dupli = false
              alert('이미 존재하는 닉네임입니다.')
              break
            } else {
              dupli = true
            }
          }
          if (dupli === true) {
            this.namedupli = true
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    checkpassword() {
      if (this.password1 === this.password2) {
        this.passwordsame = true
      } else {
        this.passwordsame = false
      }
    },
    catpick() {
      let number = this.randomnumber
      while (number == this.randomnumber) {
        number = _.random(1, 45)
      }
      this.randomnumber = number
    }
  }
}

</script>

<style>
label {
  color: white;
}

</style>