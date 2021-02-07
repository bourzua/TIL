<template>
  <div>
    <h1>Recommend</h1>
    <form>
      <select v-model="selected" @change="onChange($event)">
        <option disabled value="">select One</option>
        <option value="action">Action</option>
        <option value="animation">Animation</option>
        <option value="comedy">Comedy</option>
        <option value="romance">Romance</option>
        <option value="music">Music</option>
        <option value="thriller">Thriller</option>
        <option value="war">war</option>
      </select>
    </form>
    <span>Genre: {{selected}}</span>

    <!-- Action -->
    <div v-if="selected==='action'" class="container">
      <div class="row">
        <div v-for="movie in action_movies" :key="movie.id" class="card col-lg-4 col-md-4 col-sm-6 col-xs-12">
          <div class="col">
            <router-link :to="{name: 'Moviedetail', params: {movie_idx: movie.genre_idx, genre:'Action'}}">
              <img :src='movie.poster_path' alt="poster" width="330" height="450">
              <h7> {{ movie.title }}</h7>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- Animation -->
    <div v-if="selected==='animation'" class="container">
      <div class="row">
        <div v-for="movie in animation_movies" :key="movie.id" class="card col-lg-4 col-md-4 col-sm-6 col-xs-12">
          <div class="col">
            <router-link :to="{name: 'Moviedetail', params: {movie_idx: movie.genre_idx, genre: 'Animation'}}">
              <img :src='movie.poster_path' alt="poster" width="330" height="450">
              <h7> {{ movie.title }}</h7>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- Comedy -->
    <div v-if="selected==='comedy'" class="container">
      <div class="row">
        <div v-for="movie in comedy_movies" :key="movie.id" class="card col-lg-4 col-md-4 col-sm-6 col-xs-12">
          <div class="col">
            <router-link :to="{name: 'Moviedetail', params: {movie_idx: movie.genre_idx, genre:'Comedy'}}">
              <img :src='movie.poster_path' alt="poster" width="330" height="450">
              <h7> {{ movie.title }}</h7>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- Music -->
    <div v-if="selected==='music'" class="container">
      <div class="row">
        <div v-for="movie in music_movies" :key="movie.id" class="card col-lg-4 col-md-4 col-sm-6 col-xs-12">
          <div class="col">
            <router-link :to="{name: 'Moviedetail', params: {movie_idx: movie.genre_idx, genre:'Music'}}">
              <img :src='movie.poster_path' alt="poster" width="330" height="450">
              <h7> {{ movie.title }}</h7>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- Romance -->
    <div v-if="selected==='romance'" class="container">
      <div class="row">
        <div v-for="movie in romance_movies" :key="movie.id" class="card col-lg-4 col-md-4 col-sm-6 col-xs-12">
          <div class="col">
            <router-link :to="{name: 'Moviedetail', params: {movie_idx: movie.genre_idx, genre:'Romance'}}">
              <img :src='movie.poster_path' alt="poster" width="330" height="450">
              <h7> {{ movie.title }}</h7>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- Thriller -->
    <div v-if="selected==='thriller'" class="container">
      <div class="row">
        <div v-for="movie in thriller_movies" :key="movie.id" class="card col-lg-4 col-md-4 col-sm-6 col-xs-12">
          <div class="col">
            <router-link :to="{name: 'Moviedetail', params: {movie_idx: movie.genre_idx, genre:'Thriller'}}">
              <img :src='movie.poster_path' alt="poster" width="330" height="450">
              <h7> {{ movie.title }}</h7>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- War -->
    <div v-if="selected==='war'" class="container">
      <div class="row">
        <div v-for="movie in war_movies" :key="movie.id" class="card col-lg-4 col-md-4 col-sm-6 col-xs-12">
          <div class="col">
            <router-link :to="{name: 'Moviedetail', params: {movie_idx: movie.genre_idx, genre:'War'}}">
              <img :src='movie.poster_path' alt="poster" width="330" height="450">
              <h7> {{ movie.title }}</h7>
            </router-link>
          </div>
        </div>
      </div>
    </div>

  </div>

  
</template>

<script>

import actions from './Genres/actions.json'
import animations from './Genres/animations.json'
import comedies from './Genres/comedies.json'
import musics from './Genres/musics.json'
import romances from './Genres/romances.json'
import thrillers from './Genres/thrillers.json'
import wars from './Genres/wars.json'

export default {
  name: 'Recommend',
  data() {
    return {
      selected: '',
      action_movies: [],
      animation_movies: [],
      comedy_movies: [],
      music_movies: [],
      romance_movies: [],
      thriller_movies: [],
      war_movies: [],
    }
  },
  methods: {
    onChange() {
      this.action_movies = actions
      this.animation_movies = animations
      this.comedy_movies = comedies
      this.music_movies = musics
      this.romance_movies = romances
      this.thriller_movies = thrillers
      this.war_movies = wars
    }
  }
}
</script>

<style>

</style>