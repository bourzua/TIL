package com.example.java.day2.hiding;

class BirthDay {

    // private: 같은 클래스
    // default: 같은 패키지
    private int day;
    private int month;
    private int year;

    // 필요한 경우, 데이터 무결성을 위해 getter, setter

    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        if (month == 2){
            if(day < 1 || day > 28){
                System.out.println("날짜 오류입니다.");
            }
        }
        else {
            this.day = day;
        }
    }

    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {


        this.month = month;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
}

public class BirthDayTest{

    public static void main(String[] args) {
        BirthDay day = new BirthDay();

        day.setMonth(2);
        day.setDay(30);
        day.setYear(2018);
    }
}
