import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'
import router from '../router'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    commentlist: [],
    basemovies: [],
    movies: [],
    randommovie: '',
    watchesList: [],
    userid: -1,
    username: '익명',
    usernofear: false,
    usernothrill: false,
    usersex: '',
    usercatpic: 0,
    password: '',
    token: '',
    reviewRate: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  },
  getters: {
    randomMovie(state) { return _.sample(state.movies)},
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    DELETE_COMMENT(state, data) {
      const index = state.commentlist.indexOf(data)
      state.commentlist.splice(index, 1)
    },
    CREATE_COMMENT(state, data) {
      state.commentlist.push(data)
    },
    MOVIE_GET(state, data) {
      state.basemovies = data
      state.movies = data
    },
    CREATE_WATCH(state, data) {
      state.watchesList.push(data)
    },
    UPDATE_WATCH(state, data) {
      state.watchesList = state.watchesList.map((watch) => {
        if (watch === data) {
          watch.selected = !watch.selected
        }
        return watch
      })
    },
    SIGN_UP(state, token) {
      state.token = token
      router.push({ name: 'Login'})
    },
    FILTERING(state) {
      console.log(state.usernofear)
      console.log(state.usernothrill)
      if (state.usernofear) {
        let filtermovies = []
        for (let i=0; i<state.basemovies.length; i++) {
          let isfear = false
          for (let j=0; j<state.basemovies[i].genres.length; j++) {
            if (state.basemovies[i].genres[j].id === 27) {
              isfear = true
            }
          }
          if (isfear === false) {
            filtermovies.push(state.basemovies[i])
          }
        }
        state.movies = filtermovies
      }
      if (state.usernothrill) {
        let filtermovies2 = []
        for (let i=0; i<state.basemovies.length; i++) {
          let isthrill = false
          for (let j=0; j<state.basemovies[i].genres.length; j++) {
            if (state.basemovies[i].genres[j].id === 53) {
              isthrill = true
            }
          }
          if (isthrill === false) {
            filtermovies2.push(state.basemovies[i])
          }
        }
        state.movies = filtermovies2
      }
    },
    SAVE_TOKEN(state, data) {
      state.token = data[0]
      state.username = data[1]['username']
      state.userid = data[1]['id']
      if (data[1]['nofear'] === 'F'){
        state.usernofear = false
      } else {
        state.usernofear = true
      }
      if (data[1]['nothrill'] === 'F') {
        state.usernothrill = false
      } else {
        state.usernothrill = true
      }
      state.usersex = data[1]['sex']
      state.password = data[1]['password']
      state.usercatpic = data[1]['catpic']
      router.push({ name: 'MovieView'})
    },
    DELETE_TOKEN(state) {
      state.token = ''
      state.userid = -1
      state.username = '익명'
      state.usernofear = false
      state.usernothrill = false
      state.usersex = ''
      state.password = ''
      state.usercatpic = 0
    },
    CHANGESETTINGS(state, data) {
      console.log(data)
      if (data['nofear'] === 'F'){
        state.usernofear = false
      } else {
        state.usernofear = true
      }
      if (data['nothrill'] === 'F') {
        state.usernothrill = false
      } else {
        state.usernothrill = true
      }
    },
  },
  actions: {
    movieGet(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
        .then(res => {
          const data = _.shuffle(res.data)
          context.commit('MOVIE_GET', data)
          context.commit('FILTERING')
          // console.log(res, context)
        })
        .catch(err => console.log(err))
    },

    createWatch(context, watchList) {
      const watches = {
        title: watchList,
        selected: false,
      }
      context.commit('CREATE_WATCH', watches)
    },

    updateWatch(context, watch) {
      context.commit('UPDATE_WATCH', watch)
    },

    signUp(context, payload) {
      console.log(payload)
      axios({
        method: 'post',
        url: `${API_URL}/accounts-custom/signup/`,
        data: {
          username: payload.username,
          password: payload.password,
          sex: payload.sex,
          birth: payload.birth,
          nofear: 'F',
          nothrill: 'F',
          catpic: payload.catpic
        }
      })
        .then(res => {
          context.commit('SIGN_UP', res.data.key)
        })
        .catch(err => {
          console.log(err)
        })
    },

    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      console.log(payload)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: username, 
          password: password,
        }
      })
        .then(res => {
          const token = res.data.key
          axios({
            method: 'get',
            url: `${API_URL}/accounts/user/`,
            headers: {
              "Authorization": `Token ${token}`
            }
          })
            .then(res => {
              axios({
                method: 'get',
                url: `${API_URL}/accounts-custom/${res.data.pk}/`,
                headers: {
                  "Authorization": `Token ${token}`
                }
              })
                .then(res => {
                  console.log(12312432423)
                  console.log(res.data)
                  this.state.movies = this.state.basemovies
                  context.commit('CHANGESETTINGS', res.data[0])
                  context.commit('SAVE_TOKEN', [token, res.data[0]])
                  context.commit('FILTERING')
                })
                .catch(err => {
                  console.log(err)
                })
            })
            .catch(err => {
              console.log(err)
            })
          
        })
        .catch((err) => {
          console.log(err)
          alert('닉네임과 비밀번호를 다시 확인해주세요.')
        })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
      })
        .then(() => {
          context.commit('DELETE_TOKEN')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    changeSettings(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts-custom/${this.state.userid}/`,
        headers: {
          "Authorization": `Token ${this.state.token}`
        }
      })
        .then(res => {
          console.log(res.data)
          context.commit('CHANGESETTINGS', res.data[0])
          axios({
            method: 'get',
            url: `${API_URL}/movies/`,
          })
            .then(res => {
              const data = _.shuffle(res.data)
              context.commit('MOVIE_GET', data)
              context.commit('FILTERING')
            })
            .catch(err => console.log(err))
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteComment(context, comment) {
      context.commit('DELETE_COMMENT', comment)
    },
  },
  modules: {
  }
})
