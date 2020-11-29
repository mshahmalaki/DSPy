def my_func(lst):
    string_list = []
    for i in lst:
        if type(i).__name__ == 'str':
            string_list.append(i)
    print(string_list)
    print(len(string_list))
