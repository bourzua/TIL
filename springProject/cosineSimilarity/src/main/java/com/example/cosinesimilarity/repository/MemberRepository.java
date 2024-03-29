package com.example.cosinesimilarity.repository;

import com.example.cosinesimilarity.entity.Member;
import org.springframework.data.jpa.repository.JpaRepository;


public interface MemberRepository extends JpaRepository<Member, Long> {

    Member findByNickname(String nickname);
    Boolean existsByNickname(String nickname);
}
