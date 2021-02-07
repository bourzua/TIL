package com.study.springboot.common.security;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;

import com.study.springboot.common.security.domain.CustomUser;
import com.study.springboot.domain.Member;
import com.study.springboot.mapper.MemberMapper;

public class CustomUserDetailsService implements UserDetailsService {
	
	private static final Logger logger = LoggerFactory.getLogger(CustomUserDetailsService.class);

	@Autowired
	private MemberMapper memberMapper;

	@Override
	public UserDetails loadUserByUsername(String userName){
		logger.warn("Load User By UserName : " + userName);

		Member member = null;
		
		try {
			member = memberMapper.read(userName);
		} catch (Exception e) {
			e.printStackTrace();
		}

		logger.warn("queried by member mapper: " + member);

		return member == null ? null : new CustomUser(member);
	} 

}
