package com.example.java.doitjava.Chapter12.collection.arraylist;

import java.util.ArrayList;

class MyStack{

    private ArrayList<String> arrayStack = new ArrayList<>();

    public void push(String data) {
        arrayStack.add(data);
    }

    public String pop() {

        int len = arrayStack.size();
        if (len == 0) {
            System.out.println("스택이 비었습니다.");
            return null;
        }
        return arrayStack.remove(len - 1);
    }

    public String peek() {
        int len = arrayStack.size();
        if (len == 0) {
            System.out.println("스택이 비어있습니다.");
            return null;
        }
        return arrayStack.get(len - 1);
    }
}

public class StackTest {

    public static void main(String[] args) {

        MyStack stack = new MyStack();

        stack.push("a");
        stack.push("b");
        stack.push("c");

        System.out.println(stack.peek());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());

        System.out.println(stack.pop());
    }
}
