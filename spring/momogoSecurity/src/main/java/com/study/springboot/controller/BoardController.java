package com.study.springboot.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.annotation.Secured;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/boards")
public class BoardController {

	private static final Logger logger = LoggerFactory.getLogger(BoardController.class);
	
	@RequestMapping(value = "", method = RequestMethod.GET)
	public ResponseEntity<String> list() throws Exception {
		logger.info("list : access to all");
		
		return new ResponseEntity<>("SUCCESS", HttpStatus.OK);
	}

	@PreAuthorize("hasRole('ROLE_MEMBER')")
	@RequestMapping(value = "", method = RequestMethod.POST)
	public ResponseEntity<String> register() {
		logger.info("register : access to member");
		
		return new ResponseEntity<>("SUCCESS", HttpStatus.OK);
	}
	
	@PreAuthorize("isAuthenticated()")
	@RequestMapping(value = "/{boardNo}", method = RequestMethod.GET)
	public ResponseEntity<String> read(@RequestHeader (name="Authorization") String header, @PathVariable("boardNo") Long boardNo) {
		logger.info("read : access to authenticated user");
		logger.info("read : header = " + header);
		logger.info("read : boardNo = " + boardNo);
		
		if (header == null || !header.startsWith("Bearer ")) {
			return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }

        String authToken = header.substring(7);
        
        logger.info("read : authToken " + authToken);
        
        return new ResponseEntity<>("SUCCESS", HttpStatus.OK);
	}
	
	@PreAuthorize("hasAnyRole('ROLE_ADMIN', 'ROLE_MEMBER')")
	@RequestMapping(value = "/{boardNo}", method = RequestMethod.PUT)
	public ResponseEntity<String> modify(@PathVariable("boardNo") Long boardNo) {
		logger.info("modifyForm : access to admin or member");
		
		return new ResponseEntity<>("SUCCESS", HttpStatus.OK);
	}
	
}