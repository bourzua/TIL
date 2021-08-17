package com.example.java.java_hp.referencestatic;

public class FishBreadTest {
    public static void main(String[] args) {

        FishBread[] breads = new FishBread[4];

        breads[0] = new FishBread(0);
        breads[1] = new FishBread(1);
        breads[2] = new FishBread(2);
        breads[3] = new FishBread(3);

        for (int i = 0; i < FishBread.count; i++) {
            breads[i].print();
        }

        System.out.println("======================");

        System.out.printf("붕어빵 객체 수: %d", FishBread.count);
    }
}

class FishBread {

    // 인스턴스 변수 (non-static 필드)
    String contents;

    // 클래스 변수 (static 필드)
    static int count;

    public FishBread(int n) {
        String[] arr = {"팥", "고구마", "치즈", "슈크림"};
        contents = arr[n];

        FishBread.count++;
    }

    void print() {
        System.out.printf("[%s] 붕어빵\n", contents);
    }
}
