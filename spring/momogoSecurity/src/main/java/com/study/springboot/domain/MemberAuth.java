package com.study.springboot.domain;

import java.io.Serializable;

import lombok.Data;

@Data
public class MemberAuth implements Serializable {
	
	private static final long serialVersionUID = 1L;

	private int userId;
	private String auth;

}
