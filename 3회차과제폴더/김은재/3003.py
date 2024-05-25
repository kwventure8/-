#3003번
sol = [1,1,2,2,2,8]
abc = input().split()
result2 = ""
for i in range(6):
    j = sol[i] - int(abc[i])
    result2 = result2 + str(j) + " "
print(result2)
