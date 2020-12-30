package hello.core.member;

public class MemberServiceImpl implements MemberService {
    // 추상화에도 의존, 구체화에도 의존 ㅂㄹ
//    private final MemberRepository memberRepository = new MemoryMemberRepository();

    // 인터페이스에만 의존
    private final MemberRepository memberRepository;

    // 생성자를 통해서 MemberRepository의 구현체 선택
    // 생성자를 통해서 어떤 구현 객체가 들어올지 알 수 없다.
    public MemberServiceImpl(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Override
    public void join(Member member) {
        memberRepository.save(member);
    }

    @Override
    public Member findMember(Long memberId) {
        return memberRepository.findById(memberId);
    }
}
