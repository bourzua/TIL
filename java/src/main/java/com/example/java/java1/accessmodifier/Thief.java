package com.example.java.java1.accessmodifier;

public class Thief {
    public static void main(String[] args) {

        Wallet wallet = new Wallet(30000);
        System.out.println(wallet.toString());

//        Thief.steal(wallet);
    }

//    public static void steal(Wallet target) {
//        target.money = 0;
//    }
}

class Wallet {

    private int money;

    public Wallet(int money) {
        this.money = money;
    }

    public String toString() {
        return String.format("Wallet { money: %d }", this.money);
    }
}
