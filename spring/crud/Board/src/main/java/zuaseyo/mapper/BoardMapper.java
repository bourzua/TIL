package zuaseyo.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import zuaseyo.domain.Board;

@Mapper
public interface BoardMapper {
	
	// 게시글 목록 조회
	public List<Board> list() throws Exception;
	
	// 게시글 쓰기
	public void register(Board board) throws Exception;
	
	// 게시글 읽기
	public Board read(Integer boardNo) throws Exception;
	
	// 게시글 수정
	public void modify(Board board) throws Exception;
	
	// 게시글 삭제
	public void remove(Integer boardNo) throws Exception;
	

}
