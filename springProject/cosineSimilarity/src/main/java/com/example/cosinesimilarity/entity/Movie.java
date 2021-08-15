package com.example.cosinesimilarity.entity;

import javax.persistence.*;

@Entity
public class Movie {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private String actor;
    private String director;
    private String image;
    private String pubDate;
    private String userRating;
    private String link;

    @Column(columnDefinition = "longtext")
    private String summary;

    public Movie() {
    }

    public Movie(String title, String actor, String director, String image, String pubDate, String userRating, String link, String summary) {
        this.title = title;
        this.actor = actor;
        this.director = director;
        this.image = image;
        this.pubDate = pubDate;
        this.userRating = userRating;
        this.link = link;
        this.summary = summary;
    }

    public Long getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getActor() {
        return actor;
    }

    public String getDirector() {
        return director;
    }

    public String getImage() {
        return image;
    }

    public String getPubDate() {
        return pubDate;
    }

    public String getUserRating() {
        return userRating;
    }

    public String getLink() {
        return link;
    }

    public String getSummary() {
        return summary;
    }

    @Override
    public String toString() {
        return "Movie{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", summary='" + summary + '\'' +
                '}';
    }
}
