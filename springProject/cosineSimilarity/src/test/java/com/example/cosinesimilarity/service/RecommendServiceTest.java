package com.example.cosinesimilarity.service;

import org.assertj.core.api.Assertions;
import org.assertj.core.data.Percentage;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class RecommendServiceTest {

    @Autowired
    private RecommendService recommendService;

    @Test
    void csTest() {
        String summary = "영화는 대공황의 파도가 덮친 30년대의 뉴욕, 강변의 빈민촌에서 시작한다. 이 빈민촌은 당시 이른바 ‘잊혀진 사람 (forgotten man)이라고 불렸던 실직자와 거렁뱅이들이 집단을 이루고 살아가는 버려진 지역이다. 여기에 모피와 새틴 드레스로 무장한 두 명의 여성이 등장한다. 불록 가의 두 딸인 코넬리어와 아이린이 이 곳을 찾은 이유는 바로 자선 기금 모금 파티가 제안한 게임에 승리하기 위해서이다. 그 게임은 ‘사람들이 가장 원하지 않는 것’을 찾아 파티장에 가져오는 사람에게 우승컵을 준다는 것이다. 코넬리어와 아이린은 실직자가 최고의 품목이라는 생각에 그곳에 있던 거렁뱅이 갓프리에게 5달러를 주고 흥정하면서 서로 그를 데려가려 한다. 하지만 갓프리는 거만한 코넬리어의 요구를 무시하고 순진한 아이린의 요청을 승낙, 결국 파티에 같이 가서 아이린에게 우승컵을 선사하게 된다.<br>&nbsp; 한편 갓프리에게서 무언가 비범한 점을 발견한 아이린은 그를 집안의 새로운 집사로 고용하기에 이른다. 다음 날 빌려입은 양복으로 변신한 채, 갓프리는 불록 가의 집사로 새로운 삶을 시작하게 된다. 그러나 일주일이 멀다하고 집사가 바뀌는 불록 가의 일원들을 시중든다는 건 쉬운 일이 아니다. 못말리는 불록 집안을 참아내면서 점차 갓프리는 그를 눈엣가시로 여기는 코넬리어의 계략도 영리하게 피해가고, 안주인 안젤리카의 한심한 작태에도 적당히 추임새를 넣어주면서 이들에게 없어서는 안 될 존재가 되어버린다. 하지만 갓프리도 피해갈 수 없는 골칫거리가 생겼으니, 바로 막무가내로 집사에게 구애작전을 펼치는 철딱서니 아이린이다.<br>&nbsp; 한없이 귀엽지만 떼쟁이에 도통 말이 안 통하는 아이린은 갓프리를 곤경에 빠트리고 결국 그는 불록 집안을 나오게 된다. 하지만 하버드를 졸업한 인텔리에 좋은 가문의 자제였음에도 불구하고 공황을 체험하고자 몸소 거렁뱅이의 삶을 자청했던 갓프리의 진실이 밝혀지고, 급기야 경제적인 곤경에 빠져 모든 것을 잃게 된 불록 가문에 결정적인 도움을 주면서 비로소 불록 가의 가족들은 갓프리가 그들에게 얼마나 많은 것을 일깨워 줬는가를 깨닫게 된다.";

        double similarity1 = recommendService.getSimilarity("대공황", summary);
        double similarity2 = recommendService.getSimilarity("빈민촌", summary);
        double similarity3 = recommendService.getSimilarity("잊혀진", summary);

        double similarity = recommendService.getSimilarity("대공황 빈민촌 잊혀진", summary);

        Assertions.assertThat(similarity1).isNotEqualTo(0);
        Assertions.assertThat(similarity2).isNotEqualTo(0);
        Assertions.assertThat(similarity3).isNotEqualTo(0);

        Assertions.assertThat(similarity).isCloseTo(similarity1 + similarity2 + similarity3, Percentage.withPercentage(0.01));
    }
}