#1157번

str =input().upper()
data = {}
for key in str:
    if key not in data:
        data[key] = 1
    else:
        data[key] = data[key]+1
data = sorted(data.items(),key=lambda x:x[1])
if len(data) != 1 and data[len(data)-1][1] == data[len(data)-2][1]:
    print("?")
else:
    print(data[len(data)-1][0])
