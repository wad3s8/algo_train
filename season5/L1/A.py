first_worker = list(map(int, input().split()))
second_worker = list(map(int, input().split()))

first_left = first_worker[0]-first_worker[1]
first_right = first_worker[0]+first_worker[1]
second_left = second_worker[0]-second_worker[1]
second_right = second_worker[0]+second_worker[1]

if first_right < second_left or second_right < first_left:
    print(first_right - first_left + second_right - second_left + 2)
else:
    print(max(second_right, first_right) - min(first_left, second_left) + 1)
