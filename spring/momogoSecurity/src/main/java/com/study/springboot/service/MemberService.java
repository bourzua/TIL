package com.study.springboot.service;

import org.springframework.http.ResponseEntity;

import com.study.springboot.domain.Member;


public interface MemberService {
	
	// 회원등록
	public void register(Member member) throws Exception;
	
	// 회원조회
	public Member read(String email) throws Exception;
	
	// 로그인
	public Member login(Member member) throws Exception;

}
