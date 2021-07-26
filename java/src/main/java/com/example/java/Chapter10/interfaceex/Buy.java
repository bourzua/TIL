package com.example.java.Chapter10.interfaceex;

public interface Buy {

    void buy();

    default void order() {
        System.out.println("구매주문");
    }
}
