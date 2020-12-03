lst = [3, 2, 4, 5, 6, 7, 1, 0, 9, 8, 7]
lst_even = []
lst_odd = []

for i in lst:
    if i % 2 == 0:
        lst_even.append(i)
    else:
        lst_odd.append(i)

print('List of even numbers :', lst_even)
print('Count of odd numbers ', len(lst_odd))
