<template>
  <div>
    <h2>Community</h2>
    <br><br>
    <b-button variant="outline-info" style="float:right; margin-right: 340px"><router-link to="/createcommunity" style="color:#29c9cc">글쓰기</router-link></b-button>
    <br><br>
    <table>
    <tbody>
      <tr v-for="(community, idx) in communities" :key="idx">
        <td style="color:#3b6566">{{ community.id }}</td>
        <td><router-link :to="{name: 'CommunityDetail', params: {community_id: community.id}}" style="color:#13c8cf">{{ community.title }}</router-link></td>
        <td class="td_datetime" style="color:#3b6566">{{ $moment(community.created_at).format('YY-MM-DD') }}</td>
        <hr><hr><hr>
      </tr>
    </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
import Vue from 'vue';
import VueMoment from 'vue-moment'
Vue.use(VueMoment);


export default {
  name: 'Community',
  data () {
    return {
      communities: [],
      username: localStorage.getItem('username')
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
    getCommunities: function () {
      const config = this.setToken()

      axios.get('http://127.0.0.1:8000/communities/', config)
        .then((res) => {
          this.communities = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created: function () {
        this.getCommunities()
    },
}
</script>

<style>

.td_datetime {
    width: 110px;
    text-align: center;
}

table {
  width: 60%;
  height: 100px;
  margin: auto;
  text-align: center;
}

tr {
  border-bottom: 1px solid black;
}
</style>