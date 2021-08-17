package com.example.java.java1.oop;

public class DrinkMachineTest {
    public static void main(String[] args) {

        DrinkMachine machine1 = new DrinkMachine();
        DrinkMachine machine2 = new DrinkMachine();

        machine1.pushButton(1);
        machine2.pushButton(2);

        machine1.printOutput();
        machine2.printOutput();
    }
}

class DrinkMachine {
    String output;

    void pushButton(int num) {
        String[] drinks = {"콜라", "사이다", "맥주"};
        output = drinks[num];
    }

    void printOutput() {
        System.out.println(output);
    }
}