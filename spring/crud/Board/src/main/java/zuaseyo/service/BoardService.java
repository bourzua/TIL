package zuaseyo.service;

import java.util.List;

import zuaseyo.domain.Board;

public interface BoardService {
	
	// 게시글 목록 조회
	public List<Board> list() throws Exception;

}
