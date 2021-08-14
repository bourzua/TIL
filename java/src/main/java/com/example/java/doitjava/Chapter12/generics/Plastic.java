package com.example.java.doitjava.Chapter12.generics;

public class Plastic extends Material{

    @Override
    public String toString() {
        return "재료는 Plastic 입니다.";
    }

    @Override
    public void doPrinting() {
        System.out.println("Plastic 재료로 출력중입니다.");
    }
}
