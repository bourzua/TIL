<template>
  <div>
    <div>
    <label for="title">title: </label>
    <input type="text" v-model="title">
    </div>
    <div>
    <label for="content">content: </label>
    <textarea name="content" id="content" cols="30" rows="10" v-model="content"></textarea>
    </div>
    <b-button variant="outline-info" @click="createCommunity">글쓰기</b-button>
  </div>
  
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateCommunity',
  data () {
    return {
      title: '',
      content: '',
    }
  },
  methods: { 
    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    createCommunity () {
      const config = this.setToken()

      const communityItem = {
        title: this.title,
        content: this.content,
      }

      if (communityItem.title) {
        axios.post('http://127.0.0.1:8000/communities/', communityItem, config)
          .then(() => {
            // console.log(res)
            this.$router.push({ name: 'Community' })
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
  }

}
</script>

<style>

</style>