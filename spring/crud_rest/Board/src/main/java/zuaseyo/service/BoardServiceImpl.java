package zuaseyo.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import zuaseyo.domain.Board;
import zuaseyo.mapper.BoardMapper;

@Service
public class BoardServiceImpl implements BoardService {
	
	@Autowired
	private BoardMapper mapper;

	@Override
	public List<Board> list() throws Exception {
		return mapper.list();
	}

	@Override
	public void register(Board board) throws Exception {
		mapper.register(board);
		
	}

	@Override
	public Board read(Integer boardNo) throws Exception {
		return mapper.read(boardNo);
	}

	@Override
	public void modify(Integer boardNo, Board board) throws Exception {
		mapper.modify(boardNo, board);
	}

	@Override
	public void remove(Integer boardNo) throws Exception {
		mapper.remove(boardNo);		
	}
	
}
