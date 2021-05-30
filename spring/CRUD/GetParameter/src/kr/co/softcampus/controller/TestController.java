package kr.co.softcampus.controller;

import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.context.request.WebRequest;

@Controller
public class TestController {

	@GetMapping("/test1")
	public String test1(HttpServletRequest request) {

		String data1 = request.getParameter("data1");
		String data2 = request.getParameter("data2");
		String[] data3 = request.getParameterValues("data3");

		System.out.println("data1 : " + data1);
		System.out.println("data2 : " + data2);

		for (String str1 : data3) {
			System.out.println("data3 : " + str1);
		}

		return "result";
	}

	@PostMapping("/test2")
	public String test2(HttpServletRequest request) {

		String data1 = request.getParameter("data1");
		String data2 = request.getParameter("data2");
		String[] data3 = request.getParameterValues("data3");

		System.out.println("data1 : " + data1);
		System.out.println("data2 : " + data2);

		if (data3 != null) {
			for (String str1 : data3) {
				System.out.println("data3 : " + str1);
			}
		}
		return "result";
	}

	@GetMapping("/test3")
	public String test3(WebRequest request) {

		String data1 = request.getParameter("data1");
		String data2 = request.getParameter("data2");
		String[] data3 = request.getParameterValues("data3");

		System.out.println("data1 : " + data1);
		System.out.println("data2 : " + data2);
		for (String str1 : data3) {
			System.out.println("data3 : " + str1);
		}

		return "result";
	}

	@GetMapping("/test4/{data1}/{data2}/{data3}")
	// 형변환 가능
	public String str4(@PathVariable String data1, @PathVariable String data2, @PathVariable String data3) {
		System.out.println("data1 : " + data1);
		System.out.println("data2 : " + data2);
		System.out.println("data3 : " + data3);
		
		return "result";
	}
	
	@GetMapping("/test5")
	public String test6(@RequestParam int data1,
						@RequestParam int data2,
						@RequestParam int [] data3) {
		System.out.println("data1 : " + data1);
		System.out.println("data2 : " + data2);
		for (int a1 : data3) {
			System.out.println("data3 : " + a1);
		}
		
		return "result";
	}
	
	@GetMapping("/test7")
	public String test7(@RequestParam int data1,
						@RequestParam (required = false) String data2,
						@RequestParam (defaultValue = "0") int data3) {
		System.out.println("data1 : " + data1);
		System.out.println("data2 : " + data2);
		System.out.println("data3 : " + data3);
		
		return "result";
	}

}
