package com.example.todoList.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.todoList.Model.Todo;
import com.example.todoList.repo.TodoRepository;

@RestController
@CrossOrigin(origins="*", allowedHeaders = "*")
public class TodoController {
	
	@Autowired
	private TodoRepository todoRepo;
	
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
	
	@DeleteMapping("/todo/{todoId}")
	public String delete(@PathVariable("todoId") int todoId) {
		todoRepo.delete(todoId);
		return "OK";
	}
	
	@DeleteMapping("/todos/all")
	public String delete() {
		todoRepo.deleteAll();
		return "OK";
	}

}
