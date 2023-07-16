ls1 = [i for i in range(101)] # 0-100
ls2 = []
num = 0
while len(ls1) > 1:
    num += 1
    count = ls1.pop(0)
    if num == 3:
        ls2.append(count)
        num = 0
    else:
        ls1.append(count)
print(ls1)