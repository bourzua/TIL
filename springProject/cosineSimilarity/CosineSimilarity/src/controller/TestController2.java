package controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import beans.DataBean3;

@Controller
public class TestController2 {
	
	@PostMapping("/test1")
	public String test1(@ModelAttribute DataBean3 bean) {
//		System.out.printf("data1 : %s\n", bean.getData1());
//		System.out.printf("data2: %s\n", bean.getData2());
		
		return "test5";
	}
}
