<template>
  <div>
    <br>
    <br>
    <h1>{{ username }} 님의 프로필</h1>
    <br>
    <hr>
    <br>
    <h4>{{ username }} 님이 쓴 글 </h4>
    <br>
    <CommunitiesinProfile :communities="communities" />
    <br>
    <hr>
    <br>
    <h4>{{ username }} 님이 쓴 댓글</h4>
    <br>
    <CommentsinProfile :comments="comments" />


  </div>
</template>

<script>
import axios from 'axios'

import CommunitiesinProfile from '@/components/CommunitiesinProfile.vue'
import CommentsinProfile from '@/components/CommentsinProfile.vue'

export default {
  components: {
    CommunitiesinProfile,
    CommentsinProfile
  },
  data: function () {
    return {
      username: localStorage.getItem('username'),
      communities: [],
      comments: [],
    }
  },
  methods: {
    getUserComments: function (username) {
      axios.get( `http://127.0.0.1:8000/communities/${username}/getusercomments/`, this.setToken())
      .then((res) => {
        // console.log(res.data)
        this.comments = res.data
        console.log(this.comments)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getUserCommunities: function (username) {
      axios.get( `http://127.0.0.1:8000/communities/${username}/getusercommunities/`, this.setToken())
      .then((res) => {
        // console.log(res.data)
        this.communities = res.data
        console.log(this.communities)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    setToken: function () {
      const config = {
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }
      return config
    },

    },
    created: function () {
      this.getUserCommunities(this.username)
      this.getUserComments(this.username)
    }
  }


</script>

<style>

</style>