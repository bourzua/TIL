package controller;

import java.util.Map;

import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import beans.DataBean;
import beans.DataBean2;

@Controller
public class TestController {
	
//	@GetMapping("/test1")
//	public String test1(@RequestParam Map<String, String> map) {
//		String data1 = map.get("data1");
//		String data2 = map.get("data2");
//		
//		System.out.printf("data1 : %s\n", data1);
//		System.out.printf("data2 : %s\n", data2);
//		
//		return "result";
//	}
	
//	@GetMapping("/test2")
//	public String test2(@ModelAttribute DataBean bean1, @ModelAttribute DataBean2 bean2) {
//		System.out.printf("data1 : %d\n", bean1.getData1());
//		System.out.printf("data2 : %d\n", bean1.getData2());
//		
//		for (int number1 : bean1.getData3()) {
//			System.out.printf("data3 : %d\n", number1);
//		}
//		
//		System.out.printf("bean2.data1 : %d\n", bean2.getData1());
//		System.out.printf("bean2.data2 : %d\n", bean2.getData2());
//		
//		return "result";
//	}
	
	@GetMapping("/test1")
	public String test1() {
		return "test1";
	}
	
	@GetMapping("/test2")
	public String test2(HttpServletRequest request) {
		
		request.setAttribute("data1", 100);
		request.setAttribute("data2", 200);
		
		return "test2";
	}
	
	@GetMapping("/test3")
	public String test3(Model model) {
		
		model.addAttribute("data1", 300);
		model.addAttribute("data2", 400);
		
		return "test3";
	}
	
	@GetMapping("/test4")
	public ModelAndView test4(ModelAndView mv) {
		mv.addObject("data1", 500);
		mv.addObject("data2", 600);
		
		mv.setViewName("test4");
		
		return mv;
	}
	
	
}
