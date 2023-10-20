# 1545 거꾸로 출력해 보아요

# 주어진 숫자부터 0까지 순서대로 찍어

# sol) 그냥 빼면서 출력하면됨

N = int(input())
rst_str = ''
for i in range(N):
    rst_str = rst_str + str(N-i)
    rst_str = rst_str + ' '
# 0까지 찍어야됨
rst_str = rst_str + '0'
print(rst_str)

