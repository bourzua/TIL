package com.study.springboot.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import com.study.springboot.domain.Member;
import com.study.springboot.mapper.MemberMapper;
import com.study.springboot.service.MemberService;

@Service
public class MemberServiceImpl implements MemberService{
	
	@Autowired
	private MemberMapper mapper;

	@Override
	public void register(Member member) throws Exception {
		mapper.register(member);
		
	}

	@Override
	public Member read(String email) throws Exception {
		return mapper.read(email);
	}

	@Override
	public Member login(Member member) throws Exception {
		return mapper.login(member);
	}
	
}
