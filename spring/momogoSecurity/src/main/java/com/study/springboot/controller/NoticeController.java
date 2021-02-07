package com.study.springboot.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/notices")
public class NoticeController {

	private static final Logger logger = LoggerFactory.getLogger(NoticeController.class);

	@RequestMapping(value = "", method = RequestMethod.GET)
	public ResponseEntity<String> list() throws Exception {
		logger.info("list : access to all");
		
		return new ResponseEntity<>("SUCCESS", HttpStatus.OK);
	}

	@PreAuthorize("hasRole('ROLE_ADMIN')")
	@RequestMapping(value = "", method = RequestMethod.POST)
	public ResponseEntity<String> register() {
		logger.info("register : access to admin");
		
		return new ResponseEntity<>("SUCCESS", HttpStatus.OK);
	}

}
