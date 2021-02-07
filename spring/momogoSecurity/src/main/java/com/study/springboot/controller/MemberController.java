package com.study.springboot.controller;

import java.util.HashMap;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.ui.Model;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import com.study.springboot.domain.Member;
import com.study.springboot.service.MemberService;


@RestController
@CrossOrigin(origins = {"*"})
@RequestMapping("/user")
public class MemberController {
	
	@Autowired
	private MemberService service;	
	
	private static final Logger log = LoggerFactory.getLogger(MemberController.class);
	
	@Autowired
	private PasswordEncoder passwordEncoder;
	
	// 회원가입 처리
	@RequestMapping( value = "/join", method = RequestMethod.POST)
	public String register(@Validated @RequestBody Member member) throws Exception {
		
		System.out.println("되니?");
		
		log.info("postSignup = 회원가입 : {}", member);
		
		// 비밀번호 암호화
		String inputPassword = member.getUserPw();
		member.setUserPw(passwordEncoder.encode(inputPassword));
		
		// DB에 회원정보 등록
		service.register(member);
		
		return "Success";
	}
	
	// 로그인 처리
	@PostMapping( value = "/login" )
	public ResponseEntity<HashMap<String, String>> login(Member member) throws Exception {
		
		HashMap<String, String> map = new HashMap<String, String>();
		
		// 비밀번호 암호화
		String inputPassword = member.getUserPw();
		member.setUserPw(passwordEncoder.encode(inputPassword));
		
		Member loginUser = service.login(member);
		
		// 로그인 성공
		if( loginUser != null ) {
			
		}
		else {
			
		}
		
		ResponseEntity<HashMap<String, String>> entity = new ResponseEntity<HashMap<String,String>>(map, HttpStatus.OK);
		
		
		return entity;
	}
	
	

	
	
	
	
}
