# 문제집) Python 배우기 (1~50)
## 2754_학점계산
# 브론즈 4

grade = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
         'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
         'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
         'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
         'F' : 0.0}

score = str(input())

result = grade[score]

print(result)