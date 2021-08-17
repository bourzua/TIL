package com.example.cosinesimilarity.service;

import com.example.cosinesimilarity.dto.MovieDto;
import com.example.cosinesimilarity.entity.Movie;
import com.example.cosinesimilarity.repository.MovieRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import info.debatty.java.stringsimilarity.Cosine;

import java.util.*;

@Service
public class RecommendService {
    Cosine cosine = new Cosine();

    @Autowired
    private MovieRepository movieRepository;

    public List<MovieDto> getRecommend(String keyword) {
        List<Movie> movieList = movieRepository.findAll();

        // LinkedHashMap: 순서가 보장되는 HashMap
        LinkedHashMap<Movie, Double> movieWithSimilarity = new LinkedHashMap<>();

        for (Movie movie : movieList) {
            double similarity = cosine.similarity(keyword, movie.getSummary());
            movieWithSimilarity.put(movie, similarity);
        }

        LinkedList<Map.Entry<Movie, Double>> entries = new LinkedList<>(movieWithSimilarity.entrySet());
        Collections.sort(entries, (((o1, o2) -> o2.getValue().compareTo(o1.getValue()))));

        List<Map.Entry<Movie, Double>> subRecommendedMovies = entries.subList(0, 15);

        ArrayList<MovieDto> recommendedMovies = new ArrayList<>();

        for (Map.Entry<Movie, Double> subEntry : subRecommendedMovies) {
            Movie movie = subEntry.getKey();
            MovieDto movieDto = new MovieDto(movie.getTitle(), movie.getActor(), movie.getImage(), movie.getUserRating(), movie.getSummary());
            recommendedMovies.add(movieDto);
        }
        return recommendedMovies;
    }

    public double getSimilarity(String keyword, String summary) {
        double cs = 0;
        String[] keywords = keyword.split(" ");
        for (String k : keywords) {
            cs += cosine.similarity(k, summary);
        }
        return cs;
    }
}
