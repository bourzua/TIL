package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
	@GetMapping("/hello")
	public MyData hello() {
		MyData d = new MyData();
		d.name = "test";
		d.age = 20;
		return d;
	}
}

class MyData{
	public String name;
	public int age;
}