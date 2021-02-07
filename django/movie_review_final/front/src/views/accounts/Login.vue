<template>
  <div>
    <h1>LOGIN</h1>
    <div>
      <label for="username">ID: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">PW: </label>
      <input
      type="password"
      id="password"
      v-model="credentials.password"
      @keypress.enter="login"
      >
    </div>
    <button @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      }      
    }
  },
  methods: {
    login(event) {
      event.preventDefault()
      axios.post('http://127.0.0.1:8000/accounts/api-token-auth/', this.credentials)      
      .then((res)=>{
        localStorage.setItem('jwt',res.data.token)
        localStorage.setItem('username', this.credentials.username)
        this.$emit('login')
        this.$router.push({ name: 'Home' })
      })
      .catch((err)=>{
        console.error(err)
      })      
    },
  },
}
</script>

<style>

</style>