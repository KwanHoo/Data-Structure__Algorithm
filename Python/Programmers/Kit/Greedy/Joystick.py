# 알고리즘 고득점 KIT _ 탐욕법 -> 브루트포스??
# 조이스틱

## 조이스틱으로 알파벳 이름 완성

## 유니코드 A:65

#! 순방향으로 갈수도 있고 역방향으로 갈 수도 있음
name = input()

## 참고 풀이
def solution(name):
    # 조이스틱 조작 횟수
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i, char in enumerate(name): ## enumerate 는 인덱스 같이 해줌 (0,J), (1,A), (2,N)
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기 -> A연속 판별 부분
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신  -> 최단거리 이동 판별 부분
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])## 3가지 중 최솟값
            ## 해당 식 블로그 설명 참고하기!!
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer

## 접근2
def solution2(name):
    answer = 0
    vlist = []
    for i in range(len(name)):
        word = ord(name[i])
        sondi = abs(word - 65)
        backdi = abs(word - 90) + 1
        temp = min(sondi, backdi)
        vlist.append(temp)

    print(vlist) ## JEROEN[9, 4, 9, 12, 4, 13] =>56 / JAN [9, 0, 13] => 23

## 접근1 => 제시된 테스트 케이스 1,2 통과 but. 히든 테케에서 걸리고 있음
def solution1(name):
    answer = 0

    for i in range(len(name)):
        wn = ord(name[i])

        if wn < 79: #순방향
            answer += wn-65
        else: #역방향
            answer += 1+ abs(90-wn)


        if i == len(name)-1:    # 마지막인경우 for문 탈출 아래 실행 X
            break
        # 옆으로이동
        if name[i+1] != 'A':
            answer +=1      # 다음 글자 A아닌경우 반대로 이동
        else:               # A 인경우
            if len(name) == 3: # 3글자 단어인 경우 바로 마지막으로 넘어가기
                answer +=1
                wn = ord(name[-1]) # 마지막 단어 판별
                if wn < 79:  # 순방향
                    answer += wn - 65
                else:  # 역방향
                    answer += 1 + abs(90 - wn)
                break #!for문 탈출
            else:              # 4글자 이상 단어인 경우
                answer += 1
    print(answer)

    return answer

solution(name)
#참고
## ord() : 문자열 -> 숫자 변환
## chr() : 숫자 -> 문자열 변환