# 1928_Base64 Decoder

## 24비트 버퍼에 한 바이트(4비트)씩 3바이트 문자를 집어넣음
## 버퍼의 위쪽부터 6비트씩 잘라 그값을 읽고 각각의 값을 아래 문자로 인코딩

# 1.입력값을 인덱스값으로 변환
# 2.인덱스값을 2진수로 변환
# 3. 빈칸을 0으로 채우기
# 4. 10진수로 바꾸기 위해 8자리로 만들기 (입력값*6)//8
# 5. 아스키값, 인코딩 값으로 변환하기

# dic 리스트에 인코딩 값 넣기
dic = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/' ]

T = int(input())

for tc in range(T):
    word = list(input())                # 인코딩된 상태로 주어지는 문자열
    value = ''

    for j in range(len(word)):
        num = dic.index(word[j])        # num 변수에 dic 리스트 인덱스값 넣기

        # 2진수로 변환하고 맨 앞의 '0b'를 제거하기 위해 2번 인덱스부터 저장하기
        # integer -> 이진수(binary) 문자열로 변환 함수 : bin()
        bin_num = str(bin(num)[2:])     # 2진수의 경우 '0b'가 앞에 붙음

        ## 길이가 6이 될때까지 앞에 0을 붙여줌
        while len(bin_num) <6:
            bin_num = '0' + bin_num
        value += bin_num


    result = ''

    ## 입력받은 문자열의 길이에 6을 곱하고 8 비트씩 자른 값을
    # 반복문의 범위로 하여 자른값을 10진수로 변환하여 data에 할당하고
    # data 값을 문자형으로 변환하여 result에 추가

    ## 10진수로 변환하기 위해 8자리로 만들어줌   (입력값*6) //8
    for j in range(len(word)*6 // 8):
        # 10진수 변환
        data = int(value[j*8 : j*8+8], 2) #int(string,base) -> int('0b111100',2) =>60 : 2진수 문자열 10진수로 변환
        result += chr(data)

    print(f'#{tc+1} {result}')

