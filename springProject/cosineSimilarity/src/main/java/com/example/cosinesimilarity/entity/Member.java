package com.example.cosinesimilarity.entity;

import javax.persistence.*;

@Entity
public class Member {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String nickname;
    private String password;

    @Column(columnDefinition = "varchar(20) default '일반'")
    private String grade;

    public Member() {
    }

    public Member(String nickname, String password, String grade) {
        this.nickname = nickname;
        this.password = password;
        this.grade = grade;
    }

    public Long getId() {
        return id;
    }

    public String getNickname() {
        return nickname;
    }

    public String getPassword() {
        return password;
    }
}
