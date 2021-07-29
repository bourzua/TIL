package com.example.java.Chapter12.collection.hashset;

import java.util.HashSet;

public class HashSetTest {

    public static void main(String[] args) {

        HashSet<String> set = new HashSet<>();

        set.add("aaa");
        set.add("bbb");
        set.add("ccc");

        System.out.println(set);

        set.add("aaa");

        System.out.println(set);
    }
}
