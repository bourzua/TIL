package com.study.springboot.mapper;

import org.apache.ibatis.annotations.Mapper;

import com.study.springboot.domain.Member;

@Mapper
public interface MemberMapper {
	
	// 회원정보 등록
	public void register(Member member) throws Exception;
	
	// 회원조회
	public Member read(String email) throws Exception;
	
	// 로그인
	public Member login(Member member) throws Exception;
}
