package com.example.cosinesimilarity.dto;

public class MovieDto {

    private String title;
    private String actor;
    private String image;
    private String userRating;
    private String summary;

    public MovieDto() {
    }

    public MovieDto(String title, String actor, String image, String userRating, String summary) {
        this.title = title;
        this.actor = actor;
        this.image = image;
        this.userRating = userRating;
        this.summary = summary;
    }

    public String getTitle() {
        return title;
    }

    public String getActor() {
        return actor;
    }

    public String getImage() {
        return image;
    }

    public String getUserRating() {
        return userRating;
    }

    public String getSummary() {
        return summary;
    }
}


