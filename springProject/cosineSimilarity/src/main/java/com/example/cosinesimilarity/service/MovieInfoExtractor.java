package com.example.cosinesimilarity.service;

import com.google.gson.JsonElement;

public class MovieInfoExtractor {
    public static String getTitle(JsonElement item) {
        return item.getAsJsonObject().get("title").getAsString();
    }

    public static String getActor(JsonElement item) {
        return item.getAsJsonObject().get("actor").getAsString();
    }

    public static String getDirector(JsonElement item) {
        return item.getAsJsonObject().get("director").getAsString();
    }

    public static String getImage(JsonElement item) {
        return item.getAsJsonObject().get("image").getAsString();
    }

    public static String getPubDate(JsonElement item) {
        return item.getAsJsonObject().get("pubDate").getAsString();
    }

    public static String getUserRating(JsonElement item) {
        return item.getAsJsonObject().get("userRating").getAsString();
    }

    public static String getLink(JsonElement item) {
        return item.getAsJsonObject().get("link").getAsString();
    }
}
