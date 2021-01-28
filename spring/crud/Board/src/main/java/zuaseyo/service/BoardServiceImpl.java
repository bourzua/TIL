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
	
}
