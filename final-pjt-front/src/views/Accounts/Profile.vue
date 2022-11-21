<template>
  <div id="myprofile">
    <div id="myinfo" class="col-12" style="margin-left:5%;">
      <div style="display: flex;">
        <img id="personimg" :src="require(`@/assets/user.jpg`)" style="width:40%;">
        <div>
          <h2>{{ person.personname }}</h2>
        </div>
      </div>
      <br>
      <div style="display: flex;">
        <div>
          <h5>팔로워: {{ followerscnt }}</h5>
          <h5>팔로우: {{ followingscnt }}</h5>
        </div>
        <button type="button" class="btn btn-light" @click="followThis">Follow</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'MyProfile',
  data() {
    return {
      personname: this.$route.params.personname,
      me: [],
      person: {},
      followerscnt: 0,
      followingscnt: 0,
    }
  },
  created() {
    this.getPerson()
  },
  methods: {
    getPerson() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts-custom/usersinfo/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`
          }
      })
        .then(res => {
          const prmts = { pk: -1, personname: null }
          for (let i=0; i < res.data.length; i++) {
            if (res.data[i].username === this.personname) {
              prmts.pk = res.data[i].id
              prmts.personname = res.data[i].username
              break
            }
          }
          this.person = prmts
          this.getPersonFollow(prmts.pk)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getPersonFollow(personId) {
      console.log(personId)
      axios({
        method: 'get',
        url: `${API_URL}/accounts-custom/${personId}/followinfo/`,
        headers: {
          "Authorization": `Token ${this.$store.state.token}`
          }
      })
        .then(res => {
          console.log('++++')
          console.log(res)
          this.followerscnt = res.data.followers.length
          this.followingscnt = res.data.followings.length
        })
        .catch(err => {
          console.log(err)
        })
    },
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
              url: `${API_URL}/accounts-custom/${res.data.pk}/${this.person.pk}/follow/`,
              headers: {
                "Authorization": `Token ${this.$store.state.token}`
              }
            })
              .then(res => {
                console.log(res)
                this.getPersonFollow(this.person.pk)
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
    margin: 5%;
}

#myinfo {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  padding: 5%;
}

#mysettings {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  padding: 5%;
}

#personimg {
  border-radius: 70%;
}
</style>