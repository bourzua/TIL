package com.study.springboot.controller;

import java.security.Principal;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.study.springboot.domain.Member;
import com.study.springboot.service.MemberService;

@Controller
public class MainController {
	
	private static final Logger log = LoggerFactory.getLogger(MainController.class);

	
	@Autowired
	private MemberService service;
	
	@GetMapping("/")
	public String main(Model model, Principal principal) throws Exception {
		
		String user_email;
		
		if ( principal != null ) {
			user_email = principal.getName();
			
			Member member = service.read(user_email);
			model.addAttribute("user", member);
			
			log.info("user_email : " + user_email);
			log.info("user_nickname : " + member.getUserNickname());
			
		}		
		
		
		return "main";
	}

}
