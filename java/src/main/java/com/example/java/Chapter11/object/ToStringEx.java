package com.example.java.Chapter11.object;

class Book {
    String title;
    String author;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    @Override
    public String toString() {
        return title + "," + author;
    }
}

public class ToStringEx {

    public static void main(String[] args) {

        Book book = new Book("두잇자바", "주아님");
        System.out.println(book);

        String str = new String("test");
        System.out.println(str);
    }
}
