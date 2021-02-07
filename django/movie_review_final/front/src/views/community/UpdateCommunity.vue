<template>
  <div>
    <div>
      <label for="title">title: </label>
      <input type="text" name="title" id="title" v-model="community.title">
    </div>
    <div>
      <label for="content">content: </label>
      <textarea name="content" id="content" cols="30" rows="10" v-model="community.content"></textarea>
    </div>
    <b-button variant="outline-success" @click="updateCommunity">수정</b-button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommunityDetailUpdate',
    props: {
        community_id: Number,
    },
    data: function() {
      return {
        community: [],
      }      
    },
    methods: {
      getToken: function () {
        const token = localStorage.getItem('jwt')

        const config = {
          headers: {
            Authorization: `JWT ${token}`
          },
        }
        return config
      },
      getCommunity: function () {
        const config = this.getToken()

        const community_id = this.$route.params.community_id

        axios.get(`http://127.0.0.1:8000/communities/${community_id}/`, config)
        .then((res) => {
          this.community = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      },
      updateCommunity: function () {
        const config = this.getToken()
        
        const communityItem = {
          title: this.community.title,
          content: this.community.content,
        }

        axios.put(`http://127.0.0.1:8000/communities/${this.community_id}/delete_update/`, communityItem, config)
        .then(() => {
          this.$router.push({ name: 'CommunityDetail', params: { community_id: `${this.community.id}` }})
        })
        .catch((err) => {
          console.log(err)
        })
      },
    },
    created: function () {
      this.getCommunity()
    }

}
</script>

<style>

</style>