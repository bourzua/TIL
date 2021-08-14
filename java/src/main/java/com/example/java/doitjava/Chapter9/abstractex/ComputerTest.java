package com.example.java.doitjava.Chapter9.abstractex;

public class ComputerTest {

    public static void main(String[] args) {

//        Computer c1 = new Computer(); 추상 클래스는 인스턴스화 X
        Computer c2 = new DeskTop();
//        Computer c3 = new NoteBook();
        NoteBook c4 = new MyNoteBook();
        c2.display();
        c4.display();
    }
}
