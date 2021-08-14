package com.example.java.doitjava.Chapter10.interfaceex;

public class CustomerTest {

    public static void main(String[] args) {

        Customer customer = new Customer();

        Buy buyer = customer;
        buyer.buy();

        Sell seller = customer;
        seller.sell();


        customer.order();
        buyer.order();
        seller.order();
    }
}
