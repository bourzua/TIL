package com.example.cosinesimilarity.service;

import com.example.cosinesimilarity.dto.LoginDto;
import com.example.cosinesimilarity.entity.Member;
import com.example.cosinesimilarity.repository.MemberRepository;
import org.aspectj.lang.annotation.After;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class MemberServiceTest {

    @Autowired
    private MemberService memberService;

    @Autowired
    private MemberRepository memberRepository;

    @AfterEach
    void afterEach() {
        memberRepository.deleteAll();
    }

    @Test
    void join() {
        //given
        Member member = new Member("zuaseyo", "1234", "일반");
        //when
        Member savedItem = memberRepository.save(member);
        //then
        Member foundMember = memberRepository.findByNickname(savedItem.getNickname());
        Assertions.assertThat(foundMember.getNickname()).isEqualTo(savedItem.getNickname());

        // 객체로 assertThat하니까 계속 안돼서 보니까 저장되기 전 만들어진 객체는 id가 null이고
        // 저장된 객체는 id가 생성됐으니까 계속 안된다고 한듯?
    }

    @Test
    void joinLogin() {
        memberRepository.save(new Member("zuaseyo", "1234", "일반"));
        memberService.login(new LoginDto("zuaseyo", "1234"));
    }
}