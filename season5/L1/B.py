first_ckeck = list(map(int, input().split(':')))
second_ckeck = list(map(int, input().split(':')))
f = first_ckeck[0] + second_ckeck[0]
s = first_ckeck[1] + second_ckeck[1]
value = s-f
if value<0:
    print(0)
else:
    flag = int(input())
    if  flag == 1:
        enemy_in_visting = first_ckeck[1]
        my_in_visting = second_ckeck[0] + value
    else:
        enemy_in_visting = second_ckeck[1]
        my_in_visting = first_ckeck[0]

    if my_in_visting <= enemy_in_visting:
        value+=1
    print(value)