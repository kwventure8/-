#11005
line = input().split() 
N = int(line[0])
B = int(line[1])
sol = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #리스트or문자열
result = ""

while N > 0:
    index = N % B #나머지 연산자       N100 / 8  = 12...4 12/8 = 1...4  1/8= 0...1
    result = sol[index] + result      #맨 뒤숫자부터  나머지 추가 
    N = N // B #정수출력나눗셈 #N=12 

print(result)
