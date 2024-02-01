/* 고를 수 있는 포켓몬 최대값 - 최대한 다양한 종류의 포켓몬 원함
* N마리중 N/2 마리 가능
* return : 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아 그때의 폰켓몬 종류 번호의 개수를 return
*/
/** 풀이
* - 중복을 제거한 값을 구하기 위해 Set을 이용
* - 중복을 제거한 Set의 크기가 max 보다 크면 max를, 작으면 Set 사이즈를 리턴
*/
import java.util.*;
class Solution {
    public int solution(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for(int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }

        int answer = set.size();
        if(answer > nums.length / 2) {
            answer = nums.length / 2;
        }

        return answer;
    }
}