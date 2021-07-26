package com.example.java.Chapter11.string;

public class StringBuilderTest {

    public static void main(String[] args) {

        String str1 = new String("java");

        System.out.println(System.identityHashCode(str1));

        StringBuilder buffer = new StringBuilder(str1);
        System.out.println(buffer);

        buffer.append(" and");
        buffer.append(" android");
        System.out.println(System.identityHashCode(buffer));

        String str2 = buffer.toString();
        System.out.println(str2);

    }
}
