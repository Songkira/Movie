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
    movies: [],
    randommovie: '',
    watchesList: [],
    userid: -1,
    username: '익명',
    token: '',
  },
  getters: {
    randomMovie(state) { return _.sample(state.movies)},
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    // UPDATE_COMMENT(state, data) {
    //   state.commentlist = state.commentlist.map((comment) => {
    //     if (comment !== data) {
    //       comment.title = data 
    //     }
    //   })
    // },
    DELETE_COMMENT(state, data) {
      const index = state.commentlist.indexOf(data)
      state.commentlist.splice(index, 1)
    },
    CREATE_COMMENT(state, data) {
      state.commentlist.push(data)
    },
    MOVIE_GET(state, data) {
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
    SAVE_TOKEN(state, data) {
      state.token = data[0]
      state.username = data[1]
      if (state.token != '') {
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
            "Authorization": `Token ${data[0]}`
          }
        })
          .then(res => {
            console.log(res.data)
            state.userid = res.data.pk
            console.log(state.userid)
          })
          .catch(err => {
            console.log(err)
          })
        }
      router.push({ name: 'MovieView'})
    },
    DELETE_TOKEN(state) {
      state.token = ''
      state.username = '익명'
      // router.push({ name: 'MovieView'})
    }
  },
  actions: {
    movieGet(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
        .then(res => {
          context.commit('MOVIE_GET', res.data)
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
      axios({
        method: 'post',
        url: `${API_URL}/accounts-custom/signup/`,
        data: {
          username: payload.username,
          password: payload.password1,
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
      // const token = 'Token 6b104660bdcbe43b6703812ea9ac605aaf7e797d'
      // console.log(payload)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: username, 
          password: password,
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', [res.data.key, payload.username])
        })
        .catch((err) => {
          console.log(err)
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
    // createComment(context, comment) {
    //   const commentItem = { 
    //     content: comment
    //   }
    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/movies/{}`
    //   })
    //   // console.log(newMessage)
    //   context.commit('CREATE_COMMENT', commentItem)
    // },
    deleteComment(context, comment) {
      context.commit('DELETE_COMMENT', comment)
    },
    // updateComment(context, comment) {
    //   context.commit('UPDATE_COMMENT', comment)
    // },
  },
  modules: {
  }
})
