package com.example.java.java1.oop.constructor;

public class BicycleTest { // 시나리오 작성
    public static void main(String[] args) {

        Bicycle b1 = new Bicycle("부릉2", 21.74, 899000);
        Bicycle b2 = new Bicycle("씽씽2", 12.57, 495000);

        System.out.printf("{%s, %.2f, %d}\n", b1.name, b1.weight, b1.price);
        System.out.printf("{%s, %.2f, %d}", b2.name, b2.weight, b2.price);

    }
}

class Bicycle {
    String name;
    double weight;
    int price;

    public Bicycle(String name, double weight, int price) {
        this.name = name;
        this.weight = weight;
        this.price = price;
    }

    void move() {
        System.out.println("자전거를 타고 이동합니다.");
    }

    void horn() {
        System.out.println("따르르릉! 지나갈게요~");
    }
}