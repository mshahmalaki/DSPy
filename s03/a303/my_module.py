def find_even_num(lst):
    lst_even = []
    for i in lst:
        if i >= 0:
            lst_even.append(i)
    print(lst_even)
    print(sum(lst_even))
