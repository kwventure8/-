#25206번
N= 20
n= 0
sum = 0.0
data = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0}
for i in range(N): #20
    str1 = input().split() #과목명,학점,등급
    if str1[2] != "P":
        sum = sum + (data[str1[2]] * float(str1[1]))
        n=n+float(str1[1])
print(sum/n)
