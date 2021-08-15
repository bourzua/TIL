package com.example.cosinesimilarity.service;

import com.example.cosinesimilarity.dto.MemberDto;
import com.example.cosinesimilarity.entity.Member;
import com.example.cosinesimilarity.exception.CustomJoinException;
import com.example.cosinesimilarity.repository.MemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MemberService {

    @Autowired
    private MemberRepository memberRepository;

    public void saveMember(MemberDto memberDto) {
        if (memberRepository.existsByNickname(memberDto.getNickname())) {
            throw new CustomJoinException("중복된 아이디입니다.");
        }
        Member member = new Member(memberDto.getNickname(), memberDto.getPassword(), "일반");
    }
}
