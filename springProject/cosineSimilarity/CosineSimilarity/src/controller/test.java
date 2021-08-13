package controller;
import java.util.Map;

import info.debatty.java.stringsimilarity.Cosine;


/**
 * Example of computing cosine similarity with pre-computed profiles.
 */
public class test {

    public static void main(String[] args) throws Exception {
//        String s1 = "My first string";
//        String s2 = "My other string...";
        
        String s1 = "My";
        String s2 = "My";

        // Let's work with sequences of 2 characters...
        Cosine cosine = new Cosine(2);

        // Pre-compute the profile of strings
        Map<String, Integer> profile1 = cosine.getProfile(s1);
        Map<String, Integer> profile2 = cosine.getProfile(s2);
        
        

        // Prints 0.516185
        System.out.println(cosine.similarity(profile1, profile2));
    }
}