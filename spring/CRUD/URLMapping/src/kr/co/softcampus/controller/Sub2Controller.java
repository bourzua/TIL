package kr.co.softcampus.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/sub2")
public class Sub2Controller {
	
	@GetMapping("/test5")
	public String test5() {
		return "sub2/test5";
	}
	
	@GetMapping("/test6")
	public String test6() {
		return "sub2/test6";
	}

}
