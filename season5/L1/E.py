value = list(map(int, input().split()))

for i in range(10):
    if (value[0]*10+i) % value[1] == 0:
        value[0] = value[0]*10+i
        flag = True
        break
    else:
        flag = False

if flag == False:
    print(-1)
else:
    print(str(value[0])+('0' * (value[2] - 1)))