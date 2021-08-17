package com.example.java.java_hp.referencestatic;

public class PointTest {
    public static void main(String[] args) {
        Point p1 = new Point(0, 0);
        Point p2 = new Point(3, 4);

        double dist = Point.distance(p1, p2);

        System.out.printf("두 점 A%s, B%s 사이의 거리: %.2f", p1.toStr(), p2.toStr(), dist);

    }
}

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    String toStr() {
        return String.format("(%d, %d)", x, y);
    }

    static double distance(Point p1, Point p2) {
        double dX = p1.x - p2.x;
        double dY = p1.y - p2.y;
        return Math.sqrt((dX * dX) + (dY * dY));
    }
}