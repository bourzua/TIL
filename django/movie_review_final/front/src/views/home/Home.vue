<template>
  <div id="app" class="container">
    <!-- <h2>홈</h2> -->
    <h3>All Movies</h3>
    <div>
      <button v-if="idx !== 0" @click="left"><span class="t_left"></span></button>  Page : {{ idx+1 }}  
      <button v-if="idx < 15" @click="right"><span class="t_right"></span></button>
    </div>
    <br>
    <div class="row">
      <div v-for="movie in movies" :key="movie.id" class="card col-lg-4 col-md-4 col-sm-6 col-xs-12 " style="height:400px">
        <div class="col" style="height:400px">
          <router-link :to="{name: 'Moviedetail', params: {movie_idx: movie.genre_idx, genre: 'All'}}">
            <img :src='movie.poster_path' alt="poster" class="change-size-hover border">
            <hr>
            <div>
              <h7 style=""> {{movie.title}}</h7>
            </div>
          </router-link>
        </div>
      </div>
    </div>
    <br>                                                                                       
    <br>
    <div>
      <button v-if="idx !== 0" @click="left"><span class="t_left"></span></button>  Page : {{ idx+1 }}  
      <button v-if="idx < 15" @click="right"><span class="t_right"></span></button>
    </div>
    <br>
  </div>
</template>

<script>
import allmovies from "./movies.json";

export default {
  name: 'Home',
  data () {
    return {
      movies: [],
      idx: 0,
      wow: '',
    }
  },
  methods: {
    left: function () {
      this.idx = this.idx - 1
      this.movies = allmovies.slice(9*this.idx, 9*this.idx +9)
    },
    right: function () {
      this.idx = this.idx + 1
      this.movies = allmovies.slice(9*this.idx, 9*this.idx +9)
    },

  },
  created () {
    this.movies = allmovies.slice(9*this.idx, 9*this.idx +9)
  }
}
</script>

<style>
  .t {
    border:1px solid #CCC; border-radius:3px; padding:5px 10px; text-decoration:none; display:inline-block; color:#63F
  }
  .t_right::after{
    content: ''; display: inline-block; width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 6px solid #63F; margin:6px 0 0 3px;  
  }
  .t_left::before{
    content: ''; display: inline-block; width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-right: 6px solid #63F; margin:6px 0 0 3px;  
  }

  .change-size-hover{
      width: 260px;
      height: 320px;
      transition: all 0.1s;
    }
    .change-size-hover:hover{
      width: 320px;
      height: 390px;
      /* background-color: black; */
    }


</style>