package zuaseyo.service;

import java.util.List;

import zuaseyo.domain.Board;

public interface BoardService {
	
	// 게시글 목록 조회
	public List<Board> list() throws Exception;
	
	// 게시글 쓰기
	public void register(Board board) throws Exception;
	
	// 게시글 읽기
	public Board read(Integer boardNo) throws Exception;
	
	// 게시글 수정
	public void modify(Integer boardNo, Board board) throws Exception;
	
	// 게시글 삭제
	public void remove(Integer boardNo) throws Exception;

}
