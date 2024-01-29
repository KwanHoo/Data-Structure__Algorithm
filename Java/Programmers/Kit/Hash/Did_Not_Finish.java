/*  completion : 완주 , participant : 참가자
*  문제 단순화 하기
* 문제를 간단하게 만들어보는 것이 1단계
* 해결책 1) Sorting 한 뒤에 loop를 통해 1:1 비교를 하고, 서로 다른 항목이 나온 사람이 완주하지 못한 사람임
* 해결책 2) 해시 문제니 해시 사용하는 방법
*/
import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // 1. 두 배열을 정렬한다
        Arrays.sort(participant);   // 참가자 정렬
        Arrays.sort(completion);    // 완주자 정렬

        // 2. 두 배열이 다를 때까지 찾는다
        int i = 0;
        for(i=0;i<completion.length;i++)
            if(!participant[i].equals(completion[i]))
                break;


        // 3. 여기까지 왔다는 것은 마지막 주자가 완주하지 못했다는 의미이다.
        return participant[i];
    }
    // public static void main(String[] args){
    //     String[] part = {"leo", "kiki", "eden"};
    //     String[] comp = {"eden", "kiki"};
    //     Solution_Sort sol = new Solution_Sort();
    //     System.out.println(sol.solution(part, comp));
    // }
}
/*
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

class Solution_Hash {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>();
        for (String player : participant)
            map.put(player, map.getOrDefault(player, 0) + 1);   // 해쉬맵에 참가자 전부 추가
        for (String player : completion)
            map.put(player, map.get(player) - 1);

        Iterator<Map.Entry<String, Integer>> iter = map.entrySet().iterator();

        while(iter.hasNext()){
            Map.Entry<String, Integer> entry = iter.next();
            if (entry.getValue() != 0){
                answer = entry.getKey();
                break;
            }
        }
        return answer;
    }

    public static void main(String[] args){
        String[] part = {"leo", "kiki", "eden"};
        String[] comp = {"eden", "kiki"};
        Solution_Hash sol = new Solution_Hash();
        System.out.println(sol.solution(part, comp));
    }
}
*/