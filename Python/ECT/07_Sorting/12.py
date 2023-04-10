## 정렬 <4> 두 배열의 원소 교체

n, k = map(int, input().split())     # N과 K를 입력받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력 받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력 받기

a.sort()                # A 오름차순
b.sort(reverse=True)    # B 내림차순

# 첫번째 인덱스부터 확인하며 두배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 우너소가 B의 원소보다 크거나 같을 때, 반복문 탈출
        break
print(sum(a))
# 배열 A의 모든 원소의 합을 출력
