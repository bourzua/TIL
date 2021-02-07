<template>
	<div>
		<div>
			<h2> {{this.genre}} Movies</h2>
		</div>
		<button v-if="this.movie_idx >0 " @click="left"><span class="t_left"></span></button>
		<iframe v-if="videoURI" :src="videoURI" frameborder="0" style = "width: 1100px; height: 600px; margin-left:20px; margin-right:20px" ></iframe>
		<button v-if="this.movie_idx < this.end - 1" @click="right"><span class="t_right"></span></button>


		<br>
		<!-- <button @click="left"><span class="t_left"></span></button><img :src='movie.poster_path' alt="poster" width="350" height="480" style="margin-left:20px; margin-right:20px"><button @click="right"><span class="t_right"></span></button> -->
		<h2>제목 : {{ movie.title }}</h2>
		<h2>TMDB 평점 : {{movie.vote_average }}</h2>
		<h2>개봉일: {{movie.release_date}}</h2>
		<h2 v-if="movie.title !== movie.original_title">Original Title : {{ movie.original_title }}</h2>
		<div>
			<!-- <h5 v-if="movie.overview !== ''">줄거리 : {{ movie.overview }}</h5>	 -->
		</div>
		
	</div>
</template>

<script>
import allmovies from './movies.json'
import actionmovies from '../recommend/Genres/actions.json'
import animationmovies from '../recommend/Genres/animations.json'
import comedymovies from '../recommend/Genres/comedies.json'
import musicmovies from '../recommend/Genres/musics.json'
import romancemovies from '../recommend/Genres/romances.json'
import thrillermovies from '../recommend/Genres/thrillers.json'
import warmovies from '../recommend/Genres/wars.json'
import axios from 'axios'



export default {
	name: 'Moviedetail',
	data() {
		return {
			movie_idx: this.$route.params.movie_idx,
			genre: this.$route.params.genre,
			movies: [],
			movie: [],
			end: '',
			API_KEY: 'AIzaSyAl88yq0de7CPqmgb52OmYOMOZeamnRtpE',
			API_URL: 'https://www.googleapis.com/youtube/v3/search',
			videoURI: '',
		}
	},
	// 들어가면 작동하는..
	created() {

		// genre 받아서 movies 지정하기.
		if (this.genre==='All') {
			this.movies = allmovies;
		} else if (this.genre==='Action') {
			this.movies = actionmovies;
		} else if (this.genre==='Animation') {
			this.movies = animationmovies;
		} else if (this.genre==='Comedy') {
			this.movies = comedymovies;
		} else if (this.genre==='Music') {
			this.movies = musicmovies;
		} else if (this.genre==='Romance') {
			this.movies = romancemovies;
		} else if (this.genre==='Thriller') {
			this.movies = thrillermovies;
		} else if (this.genre==='War') {
			this.movies = warmovies;
		}
		this.end = this.movies.length
		console.log(this.end)
		// 유튜브
		this.movie = this.movies[this.movie_idx]
		const title = this.movie['title']
		const inputValue = `${title}-trailer`
		const params = {
			key: this.API_KEY,
			part: 'snippet',
			type: 'video',
			q: inputValue,
		}
		axios.get(this.API_URL, {
		params,
		})
		.then((res) => {
		const videoId = res.data.items[0].id.videoId
		this.videoURI = `https://www.youtube.com/embed/${videoId}?rel=1&mute=1&autoplay=1&controls=0&frameborder=0`
		console.log('비디오주소', this.videoURI)
		})
		.catch((err) => {
		console.log(err)
		})
	},

	methods: {
		// 왼쪽 방향키
    left: function () {
			this.movie_idx = this.movie_idx - 1	
			this.movie = this.movies[this.movie_idx]
			const title = this.movie['title']
			const inputValue = `${title}-trailer`
			const params = {
				key: this.API_KEY,
				part: 'snippet',
				type: 'video',
				q: inputValue,
			}
			axios.get(this.API_URL, {
			params,
			})
			.then((res) => {
				const videoId = res.data.items[0].id.videoId
				this.videoURI = `https://www.youtube.com/embed/${videoId}?rel=1&mute=1&autoplay=1&controls=0&frameborder=0`
				console.log('비디오주소', this.videoURI)
			})
			.catch((err) => {
			console.log(err)
			})
		},
		// 오른쪽 방향키
    right: function () {
      this.movie_idx = this.movie_idx + 1
			this.movie = this.movies[this.movie_idx]
			const title = this.movie['title']
			const inputValue = `${title}-trailer`
			const params = {
				key: this.API_KEY,
				part: 'snippet',
				type: 'video',
				q: inputValue,
			}
			axios.get(this.API_URL, {
			params,
			})
			.then((res) => {
				const videoId = res.data.items[0].id.videoId
				this.videoURI = `https://www.youtube.com/embed/${videoId}?rel=1&mute=1&autoplay=1&controls=0&frameborder=0`
				console.log('비디오주소', this.videoURI)
			})
			.catch((err) => {
			console.log(err)
			})
    },
	},
	
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
	/* .button {
		display:flex; justify-content: space-around;
	} */
</style>