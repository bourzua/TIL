package com.study.springboot.common.exception;

import java.io.Serializable;

public class ApiErrorInfo implements Serializable{

	private static final long serialVersionUID = -4521676718585992138L;
	
	private String message;

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}
	
}
