/** 경우의 수 문제
* 해결책 1) 해시를 통ㅎ해 각 type 별로 가짓수를 계산하고 총 경우의 수를 산출함
*/

// key : 옷의 종류, Value : 옷 종류의 가짓수(count)

import java.util.HashMap;
import java.util.Iterator;

class Solution {
    public int solution(String[][] clothes) {
        // 1. 옷을 종류별로 구분하기
        HashMap<String, Integer> map = new HashMap<>();
        for (String[] clothe : clothes) {
            String type = clothe[1];
            map.put(type, map.getOrDefault(type, 0) + 1);
        }

        // 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
        Iterator<Integer> it = map.values().iterator();
        int answer = 1;

        while(it.hasNext())
            answer *= it.next().intValue() + 1;

        // 3. 아무종류의 옷도 입지 않는 경우 제외하기
        return answer - 1;
    }
}