package com.example.demo.repo;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Component;

import com.example.demo.model.Todo;

@Component
public class TodoRepository {
	private List<Todo> todos = new ArrayList<>();
	
	public void insertTodo(Todo todo) {
		todos.add(todo);
	}
	
	public List<Todo> list() {
		return todos;
	}
	
	public void update(int id, String content) {
		for(Todo todo : todos) {
			if(todo.getTodoId() == id) {
				todo.setContent(content);
			}
		}
	}
	
	public void delete(int id) {
		Todo targetTodo = null;
		for(Todo todo : todos) {
			if(todo.getTodoId() == id) {
				targetTodo = todo;
				break;
			}
		}
		todos.remove(targetTodo);
	}
}
