## 백준 5585번
## 거스름돈
## 브론즈 2

coin = [500, 100, 50, 10, 5, 1]

P = int(input())

exc = 1000 - P
count = 0
for i in coin:
    if exc // i != 0:
        count += exc // i
        exc = exc % i
    else:
        pass

print(count)