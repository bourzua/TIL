package com.example.java.java1.gettersetter;
// 숨겨진 필드 변경하기 - setter
public class LockTest {
    public static void main(String[] args) {

        Lock lock = new Lock("123!@#");

        lock.setPassword("654#@!");

        System.out.println(lock.toString());

    }
}

class Lock {

    private String password;

    public Lock(String password) {
        this.password = password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String toString() {
        return String.format("Lock { password: %s }", this.password);
    }
}