year = int(input())
status = "unhappy"
current = 0
while status == "unhappy":
    current = year + 1
    current_str = str(current)
    list = []
    for i in current_str:
        list.append(i)
    for j in range(0, len(list) - 1):
        num_1 = list[j]
        next_num = list[j+1]
        first = list[0]
        last = list[-1]
        if next_num != num_1 and first != last \
                and last != list[1] \
                and list[0]!= list[2] \
                and list[-1]!= list[-2]\
                and list[-1] != list[-3]:
            status = "happy"
            continue
        else:
            status = "unhappy"
            year = current
            break

print(current)
# my long variant without count