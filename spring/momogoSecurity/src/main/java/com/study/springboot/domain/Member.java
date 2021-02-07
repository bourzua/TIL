package com.study.springboot.domain;

import java.util.Date;
import java.util.List;

import lombok.Data;

@Data
public class Member {
	private int userId;
	private String userEmail;
	private String userPw;
	private String userSex;
	private int userAge;
	private int userHeight;
	private int userWeight;
	private String userNickname;
	private Date regDate;
	private Date updDate;
	
	private List<MemberAuth> authList;
	
}

