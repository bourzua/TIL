package com.study.springboot.common.security.domain;

import java.util.Collection;
import java.util.stream.Collectors;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;

import com.study.springboot.domain.Member;


public class CustomUser extends User {
	
	
	private static final Logger log = LoggerFactory.getLogger(CustomUser.class);


	private static final long serialVersionUID = 1L;

	private Member member;

	public CustomUser(String username, String password, 
			Collection<? extends GrantedAuthority> authorities) {
		super(username, password, authorities);
		
		log.info("@CustomUser");
		log.info(member.toString());
	}

	public CustomUser(Member member) {

		super(member.getUserEmail(), member.getUserPw(), member.getAuthList().stream()
				.map(auth -> new SimpleGrantedAuthority(auth.getAuth())).collect(Collectors.toList()));

		this.member = member;
		log.info("@CustomUser");
		log.info(member.toString());
	}

	public Member getMember() {
		return member;
	}
}
