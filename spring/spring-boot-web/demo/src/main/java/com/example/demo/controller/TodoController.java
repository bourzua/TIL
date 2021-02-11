package com.example.demo.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.model.Todo;
import com.example.demo.repo.TodoRepository;

@RestController
public class TodoController {
	@Autowired private TodoRepository todoRepo;
	
	@GetMapping("/todos")
	public List<Todo> list() {	
		return todoRepo.list();
	}
	
	@PostMapping("/todo")
	public String create(@RequestParam("content") String content) {
		Todo todo = new Todo(content);
		todoRepo.insertTodo(todo);
		return "OK";
	}
	
	@PutMapping("/todo/{todoId}")
	public String update(@PathVariable("todoId") int todoId,
						 @RequestParam("content") String content) {
		todoRepo.update(todoId, content);
		return "OK";
	}
	
	@DeleteMapping("/todo/{todoId}")
	public String delete(@PathVariable("todoId") int todoId) {
		todoRepo.delete(todoId);
		return "OK";
	}
}
