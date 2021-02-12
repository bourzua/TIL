package com.example.todoList.Model;

public class Todo {
	private String content;
	private int todoId;
	
	private static int lastTodoId = 0;
	
	public Todo(String content) {
		lastTodoId ++;
		this.setTodoId(lastTodoId);
		this.setContent(content);
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	public int getTodoId() {
		return todoId;
	}

	public void setTodoId(int todoId) {
		this.todoId = todoId;
	}
}
