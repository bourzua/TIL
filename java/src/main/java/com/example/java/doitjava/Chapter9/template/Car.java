package com.example.java.doitjava.Chapter9.template;

public abstract class Car {

    // 추상 메서드는 하위 클래스에서 구현해야 할 의무가 있음
    public abstract void drive();
    public abstract void stop();

    public abstract void wiper();

    public void washCar() {

    }

    public void startCar() {
        System.out.println("시동을 켭니다.");
    }

    public void turnOff() {
        System.out.println("시동을 끕니다.");
    }

    // 템플릿 메서드
    public final void run() {
        startCar();
        drive();
        wiper();
        stop();
        washCar();
        turnOff();
    }
}
