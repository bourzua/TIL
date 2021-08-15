package com.example.cosinesimilarity.service;

import com.example.cosinesimilarity.entity.Movie;
import com.example.cosinesimilarity.repository.MovieRepository;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

@Service
public class MovieService {
    
    private final RestTemplate restTemplate2 = new RestTemplate();
    private final Pattern p = Pattern.compile("(<p class=\"con_tx\">)(.*)(</p>)");

    @Autowired
    private MovieRepository movieRepository;

    public void saveMovies(String keyword) {
        String apiContents = getMovieListByApi(keyword);
        JsonArray items = JsonParser.parseString(apiContents).getAsJsonObject().get("items").getAsJsonArray();
        for (JsonElement item : items) {
            String title = MovieInfoExtractor.getTitle(item);
            String title1 = title.replace("<b>", "");
            String title2 = title1.replace("</b>", "");

            String actor = MovieInfoExtractor.getActor(item);
            String director = MovieInfoExtractor.getDirector(item);
            String image = MovieInfoExtractor.getImage(item);
            String pubDate = MovieInfoExtractor.getPubDate(item);
            String userRating = MovieInfoExtractor.getUserRating(item);
            String link = MovieInfoExtractor.getLink(item);
            String replacedlink = link.replace("nhn", "naver");
            String summary = extractSummary(replacedlink);

            if (summary.equals("")) {
                continue;
            }

            Movie movie = new Movie(title2, actor, director, image, pubDate, userRating, link, summary);
            movieRepository.save(movie);
        }
    }

    public String getMovieListByApi(String keyword) {
        RestTemplate restTemplate = new RestTemplateBuilder(restTemplate1 -> {
            restTemplate1.getInterceptors().add((request, body, execution) -> {
                request.getHeaders().add("X-Naver-Client-Id", "AKJRsxXmG6aD5s8Ge3ZR");
                request.getHeaders().add("X-Naver-Client-Secret", "3VvJnIJCpV");
                return execution.execute(request, body);
            });
        }).build();
        String forObject = restTemplate.getForObject("https://openapi.naver.com/v1/search/movie.json?query="+keyword+"&display=100", String.class);
//        System.out.println(forObject);
        return forObject;
    }
    
    public String extractSummary(String link) {
        String linkContents = restTemplate2.getForObject(link, String.class);
//        System.out.println(linkContents);
        Matcher m = p.matcher(linkContents);
        String summary = "";
        while (m.find()) {
            summary = m.group(2);
        }
        return summary;
    }
}
