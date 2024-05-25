#10988번
str1 = input()
reverse = ""
for c in str1:
    reverse = c + reverse
if str1 == reverse:
    print("1")
else:
    print("0")
    
