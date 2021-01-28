package zuaseyo.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import zuaseyo.domain.Board;

@Mapper
public interface BoardMapper {
	
	// 게시글 목록 조회
	public List<Board> list() throws Exception;
	

}
