#2941번
str1 = input()
data = ["c=","c-","dz=","d-","lj","nj","s=","z="]
n = 0
for i in data:
    str1 = str1.replace(i," ")
print(len(str1))
