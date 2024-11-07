n = int(input())
list_space = []
for i in range(n):
    list_space.append(int(input()))


def click_counter(count):
    sum_click = 0
    sum_click += count // 4
    count = count % 4
    if count == 1:
        sum_click += 1
    elif count == 2:
        sum_click += 2
    elif count == 3:
        sum_click += 2
    return sum_click

sum = 0
for val in list_space:
    sum += click_counter(val)

print(sum)
