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
    usernofear: false,
    usernothrill: false,
    usersex: '',
    password: '',
    token: '',
    reviewRate: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    genrelist: {},
    yearname: [ '80년대', '90년대', '2000년대' , '2010년대', '2020년대'],
    genrename: [
      '전체',"액션","모험","애니메이션","코미디","범죄","다큐멘터리","드라마","가족","판타지",
      "역사","공포","음악","미스터리","로맨스","SF","TV 영화","스릴러","전쟁","서부"],
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
      if (state.usernofear) {
        let filtermovies = []
        for (let i=0; i<state.movies.length; i++) {
          if (state.movies[i].genres.includes(27)) {
            continue
          } else {
            filtermovies.push(state.movies[i])
          }
        }
        state.movies = filtermovies
      }
      if (state.usernothrill) {
        let filtermovies2 = []
        for (let i=0; i<state.movies.length; i++) {
          if (state.movies[i].genres.includes(53)) {
            continue
          } else {
            filtermovies2.push(state.movies[i])
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
    GENRE_GET(state, data) {
      state.genrelist = data
    },
    // STATE_GET(state, data) {
    //   state.statelist = data
    // },
    // DATE_GET(state, data) {
    //   state.datelist = data
    // },
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
          context.commit('FILTERING', { 'nofear': this.state.usernofear, 'nothrill': this.state.usernothrill })
          // console.log(res, context)
        })
        .catch(err => console.log(err))
    },

    // stateGet(context) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/movies/`,
    //   })
    //     .then(res => {
    //       context.commit('STATE_GET', res.data.production_countries_name
    //       )
    //     })
    //     .catch(err => console.log(err))
    // },

    genreGet(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/genres/`,
      })
        .then(res => {
          context.commit('GENRE_GET', res.data)
          console.log(res.data, context)
        })
        .catch(err => console.log(err))
    },

    // dateGet(context) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/movies`,
    //   })
    //     .then(res => {
    //       context.commit('DATE_GET', res.data)
    //       // console.log(res, context)
    //     })
    //     .catch(err => console.log(err))
    // },

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
                  context.commit('SAVE_TOKEN', [token, res.data[0]])
                  // context.commit('FILTERING', { 'nofear': res.data[0]['nofear'], 'nothrill': res.data[0]['nothrill'] })
                  this.movieGet()
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
          // context.commit('FILTERING', { 'nofear': res.data[0]['nofear'], 'nothrill': res.data[0]['nothrill'] })
          this.movieGet()
        })
        .catch(err => {
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
