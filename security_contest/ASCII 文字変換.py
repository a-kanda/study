# coding: utf-8

data = input().split()
after_data = []
for i in data:
    if len(i) >= 5:
        after_data.append(int(i,2))
    elif i[0] == '0':
        after_data.append(int(i,8))
    elif i.isdigit():
        after_data.append(int(i))
    else:
        after_data.append(int(i,16))

print()
for i in after_data:
    print(chr(i),end="")