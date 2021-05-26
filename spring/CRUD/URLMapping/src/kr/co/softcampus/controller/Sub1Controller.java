package kr.co.softcampus.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class Sub1Controller {
	
	@GetMapping("/sub1/test3")
	public String sub1Test3() {
		return"sub1/test3";
	}
	@GetMapping("/sub1/test4")
	public String sub1Test4() {
		return"sub1/test4";
	}

}
