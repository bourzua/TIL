import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/home/Home.vue'
import Recommend from '../views/recommend/Recommend.vue'
import Community from '../views/community/Community.vue'
import CreateCommunity from '../views/community/CreateCommunity.vue'
import Profile from '../views/accounts/Profile.vue'
import Login from '../views/accounts/Login.vue'
import Signup from '../views/accounts/Signup.vue'
import CommunityDetail from '../views/community/CommunityDetail.vue'
import UpdateCommunity from '../views/community/UpdateCommunity.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/createcommunity',
    name: 'CreateCommunity',
    component: CreateCommunity
  },
  {
    path: '/communitydetail',
    name: 'CommunityDetail',
    component: CommunityDetail
  },
  {
    path: '/updatecommunity',
    name: 'UpdateCommunity',
    component: UpdateCommunity,
    props: true,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
 
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
