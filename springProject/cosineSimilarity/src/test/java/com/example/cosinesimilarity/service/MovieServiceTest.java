package com.example.cosinesimilarity.service;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class MovieServiceTest {

    @Autowired
    private MovieService movieService;

    @Test
    void movieApi() {
        movieService.getMovieListByApi("코미디");
    }

    @Test
    void linkContents() {
        movieService.extractSummary("https://movie.naver.com/movie/bi/mi/basic.naver?code=197283");
    }

    @Test
    void extractSummary() {
        String summary = movieService.extractSummary("https://movie.naver.com/movie/bi/mi/basic.naver?code=197283");
        System.out.println(summary);
    }

    @Test
    void saveMovie() {
        movieService.saveMovies("코미디");
    }

}