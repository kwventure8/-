#2675번

T = int(input())
for i in range(T):
    str1 = input().split()
    N = int(str1[0])
    result = ""
    for j in str1[1]:
        result = result + j*N
    print(result)
        
