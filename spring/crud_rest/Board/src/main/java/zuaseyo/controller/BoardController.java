package zuaseyo.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import zuaseyo.domain.Board;
import zuaseyo.service.BoardService;


@RestController
@RequestMapping("/board")
public class BoardController {
	
	@Autowired
	private BoardService service;
	
	// 게시글 목록 조회
	@GetMapping("")
	public ResponseEntity<List<Board>> list() throws Exception {
		
		List<Board> boardList = service.list();
		ResponseEntity<List<Board>> entity = new ResponseEntity<>(boardList, HttpStatus.OK);
		return entity;
	}
	
	// 게시글 쓰기 처리
	@PostMapping("/register")
	public ResponseEntity<String> register(Board board) throws Exception {
		
		service.register(board);
		ResponseEntity<String> entity = new ResponseEntity<>("SUCCESS", HttpStatus.OK);
		
		return entity;
	}
	
	// 게시글 읽기 화면
	@GetMapping("/{boardNo}")
	public ResponseEntity<Board> read(@PathVariable("boardNo") int boardNo) throws Exception {
		
		Board board = service.read(boardNo);
		
		ResponseEntity<Board> entity = new ResponseEntity<>(board, HttpStatus.OK);
		
		return entity;
	}
	
	
	// 게시글 수정 처리
	@PutMapping("/{boardNo}")
	public ResponseEntity<String> modify(@PathVariable Integer boardNo, Board board) throws Exception {
		
		service.modify(boardNo, board);
		ResponseEntity<String> entity = new ResponseEntity<>("SUCCESS", HttpStatus.OK);
		
		return entity;
	}
	
	// 게시글 삭제 처리
	@DeleteMapping("/{boardNo}")
	public ResponseEntity<String> remove(@PathVariable("boardNo") Integer boardNo) throws Exception {
		
		service.remove(boardNo);
		ResponseEntity<String> entity = new ResponseEntity<>("SUCCESS", HttpStatus.OK);
		
		return entity;
	}
}
