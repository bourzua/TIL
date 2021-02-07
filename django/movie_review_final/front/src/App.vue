<template>
  <div id="app">
    <b-navbar toggleable type="dark" class="navbar-default fixed-top">
        <b-navbar-brand style="color:black"><router-link to="/">Movie</router-link></b-navbar-brand>
        <b-navbar-toggle target="navbar-toggle-collapse" style="color:#3b6566">
        </b-navbar-toggle>
        <b-collapse id="navbar-toggle-collapse" is-nav>
          <b-navbar-nav class="ml-auto">
            <span v-if="login">
              <!-- <b-nav-item ><router-link to="/home" style="color:#3b6566">Home</router-link></b-nav-item> -->
              <b-nav-item><router-link to="/recommend" style="color:#3b6566">Recommend</router-link></b-nav-item>
              <b-nav-item><router-link to="/community" style="color:#3b6566">Community</router-link></b-nav-item>
              <b-nav-item><router-link to="/profile" style="color:#3b6566">Profile</router-link></b-nav-item>
              <b-nav-item><router-link @click.native="logout" to="#" style="color:#3b6566">Logout</router-link></b-nav-item>
            </span>
            <span v-else>
              <b-nav-item><router-link to="/login" style="color:#3b6566">Login</router-link></b-nav-item>
              <b-nav-item><router-link to="/signup" style="color:#3b6566">Signup</router-link></b-nav-item>
            </span>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
  <router-view @login="setLogin" />
  </div>    
</template>

<script>

export default {
  data() {
    return {
      login: false,
    }
  },
  methods:{
    logout: function () {
      localStorage.removeItem('jwt')
      localStorage.removeItem('username')
      this.login = false
      this.$router.push({ name: 'Login' })
    },
    setLogin() {
      this.login = true
    },
  },
  created () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.login = true
    }
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.navbar-default { background-color: #a9ced7; }


.ceiling {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
}
</style>
