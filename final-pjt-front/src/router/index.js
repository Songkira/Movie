import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/Movies/MovieView.vue'
import RandomView from '../views/Movies/RandomView.vue'
import MyPageView from '../views/Accounts/MyPageView.vue'
import SignUpView from '../views/Accounts/SignUpView.vue'
import LoginView from '../views/Accounts/LoginView.vue'
import MySettings from '../views/Accounts/MySettings.vue'
import DetailView from '@/views/Movies/DetailView.vue'
import RecommendView from '../views/Movies/RecommendView.vue'
import ReviewsView from '../views/Accounts/ReviewsView.vue'
import NotFound from '../views/404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/mysettings',
    name: 'MySettings',
    component: MySettings
  },
  {
    path: '/movies',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/reviews/:username',
    name: 'ReviewsView',
    component: ReviewsView
  },
  {
    path: '/random',
    name: 'RandomView',
    component: RandomView
  },
  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: '/mypage/:personname',
    name: 'MyPage',
    component: MyPageView
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUpView
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView
  },
  {
    path: '/*',
    name: 'notFound',
    component: NotFound
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router