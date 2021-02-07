<template>
  <div>
    <br>
    <h1>{{ community.title }}</h1>
    created at: {{ $moment(community.created_at).format('YY-MM-DD HH:mm') }} | updated at: {{ $moment(community.updated_at).format('YY-MM-DD HH:mm') }} | {{ community.user.username }}
    <br>
    <br>
    <h5 class="container">{{ community.content }}</h5>
    <span v-if="this.username === community.user.username">
      <b-button variant="outline-danger" @click="deleteCommunity">삭제</b-button> <b-button variant="outline-success" @click="moveToUpdateCommunity">수정</b-button> <router-link to="/community"><b-button variant="outline-primary">뒤로</b-button></router-link>
    </span>
    <br>
    <br>
    <hr>
    <CommentsList :comments="comments" :username="username" @deleteComment="deleteComment" />
    <Comments @createComment="createComment" />
  </div>
</template>

<script>
import axios from'axios'
import Comments from '@/components/Comments.vue'
import CommentsList from '@/components/CommentsList.vue'


export default {
  name: 'CommunityDetail',
  components: {
    Comments,
    CommentsList,
  },
  // props: {
  //   community_id: {
  //     type: Number,
  //   }
  // },
  data () {
    return {
     community_id: this.$route.params.community_id,
     community: [],
     username: localStorage.getItem('username'),
     comment: '',
     comments: [],
     commnet_id: '',
    }
  },
  methods: {
    setToken: function () {
      const config = {
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      }
      return config
    },
    deleteCommunity: function() {
      axios({
        url: `http://127.0.0.1:8000/communities/${this.community_id}/delete_update/`,
        method: 'DELETE',
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
      .then(()=>{
        this.$router.push({ name: 'Community' })
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    moveToUpdateCommunity: function() {
      this.$router.push({name:'UpdateCommunity', params: {community_id: this.community_id}})
    },
    createComment: function (comment) {   
      this.comment = comment,
      axios({
        url: `http://127.0.0.1:8000/communities/${this.community_id}/comments/`,
        method: 'POST',
        data: {
          content: this.comment
        },
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
      .then((res) => {
        console.log(res.data)
        this.comments.push(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getComments: function () {
      const config = this.setToken()
      axios.get(`http://127.0.0.1:8000/communities/${this.community_id}/comments/get/`, config)
      .then((res) => {
        this.comments = res.data
      })
      .catch((err) => {
        console.log(err)
      })

    },
    deleteComment: function (comment_id) {
      const config = this.setToken()
      this.comment_id = comment_id
      axios.delete(`http://127.0.0.1:8000/communities/comments/${this.comment_id}/delete`, config)
      .then((res) => {
        console.log(res.data)

        this.comments.pop(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
  created() {
    
    const config = this.setToken()

    axios.get(`http://127.0.0.1:8000/communities/${this.community_id}/`, config)
    .then((res)=>{
      this.community = res.data
    })
    .catch((err) => {
      console.log(err)
    })

    this.getComments()
  }
}
</script>

<style>

</style>

