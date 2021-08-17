package com.example.java.java1.accessmodifier;

// 접근 제한자가 없을 때
public class Main {
    public static void main(String[] args) {

        Account account = new Account(1000000);
        System.out.println(account.toString());

        Hacker.malcious(account);

        System.out.println(account.toString());


    }
}

class Account {

    int balance; // 디폴트 접근 제한자 -> 같은 공간 클래스에게 공개

    public Account(int balance) {
        this.balance = balance;
    }

    public String toString() {
        return String.format("Account { balance: %d }", this.balance);
    }
}

class Hacker {
    public static void malcious(Account account) {
        account.balance = 0;
    }
}