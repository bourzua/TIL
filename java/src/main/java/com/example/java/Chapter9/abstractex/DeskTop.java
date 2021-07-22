package com.example.java.Chapter9.abstractex;

public class DeskTop extends Computer{
    @Override
    public void display() {
        System.out.println("DeskTop display()");
    }

    @Override
    public void typing() {
        System.out.println("DeskTop typing()");
    }

    public void turnOn() {
        System.out.println("DeskTop turnOn()");
    }
}
