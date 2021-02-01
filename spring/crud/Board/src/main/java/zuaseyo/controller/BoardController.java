package zuaseyo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import zuaseyo.domain.Board;
import zuaseyo.service.BoardService;


@Controller
@RequestMapping("/board")
public class BoardController {
	
	@Autowired
	private BoardService service;
	
	// 게시글 목록 조회
	@GetMapping("/list")
	public void list(Model model) throws Exception {
		
		model.addAttribute("list", service.list());
	}
	
	// 게시글 쓰기 화면
	@GetMapping("/register")
	public void registerForm(Model model) throws Exception {
	
	}
	
	// 게시글 쓰기 처리
	@PostMapping("/register")
	public String register(Model model, Board board) throws Exception {
		
		service.register(board);
		model.addAttribute("msg", "등록이 완료되었습니다.");
		
		return "board/success";
	}
	
	// 게시글 읽기 화면
	@GetMapping("/read")
	public void read(Model model, Integer boardNo) throws Exception {
		
		model.addAttribute("board", service.read(boardNo));
	}
	
	// 게시글 수정 화면
	@GetMapping("/modify")
	public void modifyform(Model model, Integer boardNo) throws Exception {
		
		model.addAttribute("board", service.read(boardNo));
	}
	
	// 게시글 수정 처리
	@PostMapping("/modify")
	public String modify(Model model, Board board) throws Exception {
		
		service.modify(board);
		model.addAttribute("msg", "수정이 완료되었습니다.");
		
		return "board/success";
	}
	
	// 게시글 삭제 처리
	@PostMapping("/remove")
	public String remove(Model model, Integer boardNo) throws Exception {
		
		service.remove(boardNo);
		model.addAttribute("msg", "삭제가 완료되었습니다.");
		
		return "board/success";
	}
}
