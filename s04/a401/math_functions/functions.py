def list_average(lst):
    return sum(lst)/len(lst)


def compare_avg(column_avg, row_avg):
    if column_avg > row_avg:
        return 'Column average is greater than row average'
    elif row_avg > column_avg:
        return 'Row average is greater than column average'
    else:
        return 'Row average is equal column average'
