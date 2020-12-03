list_1 = [3, 2, 4, 5, 6, 7, 1, 0, 9, 8, 7]
list_2 = [5, 7, 9, 1, 6, 7, 8, 3, 5, 6, 7]

for i in range(0, min(len(list_1), len(list_2))):
    if list_1[i] > list_2[i]:
        print(f'{i+1}rd item of list_1 is greater than {i+1}rd item of list_2')
        break
