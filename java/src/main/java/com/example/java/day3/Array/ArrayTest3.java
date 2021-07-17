package com.example.java.day3.Array;

public class ArrayTest3 {
    public static void main(String[] args) {

        char[] alphabets = new char[26];
        char ch = 'A';

        for (int i = 0; i < alphabets.length; i++, ch++) {
            alphabets[i] = ch;
        }
        for (int i = 0; i < alphabets.length; i++) {
            System.out.println(alphabets[i]);
        }
    }
}
