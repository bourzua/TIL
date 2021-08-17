package com.example.java.java_hp.referencestatic;

public class TeamTest {
    public static void main(String[] args) {

        Player2 kim = new Player2("Kim", new int[]{9, 8, 10});
        Player2 lee = new Player2("Lee", new int[]{10, 9, 10});
        Player2 park = new Player2("Park", new int[]{8, 10, 9});

        Player2[] koreaPlayers = { kim, lee, park };

        Team korea = new Team("KOREA", koreaPlayers);

        korea.printTeamPoints();

    }
}

class Team {
    String name;
    Player2[] players;

    public Team(String n, Player2[] p) {
        name = n;
        players = p;
    }

    void printTeamPoints() {
        int sum = 0;
        for (int i = 0; i < players.length; i++) {
            sum += players[i].totalPoints();
        }
        System.out.printf("%s -> %d points", name, sum);
    }
}

class Player2 {
    String name;
    int[] points;

    public Player2(String n, int[] p) {
        name = n;
        points = p;
    }

    int totalPoints() {
        int sum = 0;
        for (int i = 0; i < points.length; i++) {
            sum += points[i];
        }
        return sum;
    }
}
