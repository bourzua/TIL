package com.example.java.Chapter10.interfaceex;

public class CalculatorTest {

    public static void main(String[] args) {

        int num1 = 10;
        int num2 = 2;

        // 타입 상속
        Calc calc = new CompleteCalc();

        System.out.println(calc.add(num1, num2));
        calc.description();

        // 정적 메서드: 인스턴스 호출 X
        int[] arr = {1, 2, 3, 4, 5};
        int sum = Calc.total(arr);
        System.out.println(sum);

    }
}
