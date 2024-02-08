# 알고리즘 고득점 KIT _ 해시
# 전화번호 목록


# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false
# 그렇지 않으면 true를 리턴


# 해결책 1) 2중  loop를 통해 서로가 서로의 접두어인지 전부 확인
# 해결책 2) 해시를 통해 접두어가 존재하는지를 확인하는 방법

phone_book = list(map(str, input().split()))


# 참고 해쉬맵 사용
def solution(phone_book):
    # 1. Hash map을 만든다
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    # print(hash_map)     #{'119': 1, '5434': 1, '119234': 1}
    # print(list(hash_map))#['119', '5434', '119234']

    # 2. 접두어가 Hash map에 존재하는지 찾는다
    for phone_number in phone_book:
        jubdoo = ""
        # print('1',phone_number)
        for number in phone_number:
            jubdoo += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            # print('2',number, jubdoo)
            if jubdoo in hash_map and jubdoo != phone_number:
                # print('3',jubdoo, hash_map)
                return False
    return True


def solution1(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book)):
        temp = phone_book[i]
        for j in range(len(phone_book)):        ## 양방향 비교시 시간초과
            if i == j:
                continue
            else:
                comp = phone_book[j]
                if len(temp) <= len(comp):      ## temp가 더 짧은 번호
                    if temp == comp[:len(temp)]: ## 접두사 O
                        answer = False
                        return answer
                else:                           ## temp가 더 긴 번호
                    if comp == temp[:len(comp)]:
                        answer = False
                        return answer

    return answer


x =solution(phone_book)
print(x)

## 24.02.08 : 9m  (시간초과 2/4뜸) 91.7/100

#참고) 해시 get / puy / getOrDefault
# - Key:value 형태의 자료구조 ,( 해시 = 전화번호부 )
# - 해시는 모든 데이터 타입으로 접근 가능
## 예시
# - HashMap.put("A", true)
# - HashMap["A"] = true
# 불러오기 - x = HashMap.get("a")    or x = HashMap["A"]
## getOrDefault("A",flase) : A가 있다면, A의 Value를 반환 , A가 없다면 false를 반환
    # - Key가 없을때의 예외처리를 함수내에서 해줌


##!!! 해시 사용해야할때  : String을 기반으로 정보를 기록하고 관리해야 될 때
    # ->단순 배열을 쓸수 없으니 해시를 활용하자!
