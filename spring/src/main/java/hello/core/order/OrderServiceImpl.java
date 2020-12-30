package hello.core.order;

import hello.core.discount.DiscountPolicy;
import hello.core.discount.FixDiscountPolicy;
import hello.core.discount.RateDiscountPolicy;
import hello.core.member.Member;
import hello.core.member.MemberRepository;
import hello.core.member.MemoryMemberRepository;

public class OrderServiceImpl implements OrderService {
    // 인터페이스에만 의존
    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        // 주문 생성 요청이 오면
        // 1. 회원 정보를 조회
        Member member = memberRepository.findById(memberId);
        // 할인에 대해서 discountPolicy가 알아서 하도록 설계
        // 할인에 대한 변경이 필요하면 할인 쪽만 고치면 됨
        // 단일 체계 원칙?

        // 2. 할인 정책에 회원을 넘김
        int discountPrice = discountPolicy.discount(member, itemPrice);
        // 3. 최종 생성된 주문 반환
        return new Order(memberId, itemName, itemPrice, discountPrice);
    }
}
