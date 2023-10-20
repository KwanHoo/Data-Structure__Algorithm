# 1대1 가위바위보

# 가위 1, 바위 2, 보 3
# 입력으노 AB 낸거 주어짐
# 주의)비기는 경우는 없음

## 경우의 수
# 가위 보      => 1 3      : A
# 가위 바위     => 1 2      : B
# 바위 가위     => 2 1      : A
# 바위 보      => 2 3      : B
# 보 가위      => 3 1      : B
# 보 바위      => 3 2      : A

A, B = map(int, input().split())

if A == 1: # A 가위
    if B == 3:
        print('A')
    else:
        print('B')
elif A == 2: # A 바위
    if B == 1:
        print('A')
    else:
        print('B')
elif A == 3: # A 보
    if B == 3:
        print('B')
    else:
        print('A')
else:
    print('비기는 경우는 없음')
