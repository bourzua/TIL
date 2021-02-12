package com.example.todoList.repo;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Component;

import com.example.todoList.Model.Todo;

@Component
public class TodoRepository {
	
	private List<Todo> todos = new ArrayList<>();
	
	public List<Todo> list() {
		return todos;
	}
	
	public void insertTodo(Todo todo) {
		todos.add(todo);
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
	
	public void deleteAll() {
		todos.clear();
	}
}
