n = int(input())
for i in range(n+1):
    print(' '* (n-i),'*' * i)
    i += 1

#위의 코드가 백준에서 "출력 형식이 잘못되었습니다" 결과를 리턴
#다음과 같이 오류 수정
#(1) 불필요한 i += 1
#for 루프 자체가 i 값을 증가시킨다
#(2) for문의 범위
#range(n)은 0부터 n-1까지를 의미한다 => 1부터임을 명시해주어야함

n = int(input())
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)
