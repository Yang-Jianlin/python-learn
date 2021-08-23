def flatten(nested):
    for sublist in nested:
        for num in sublist:
            yield num


list_num = [[1, 2, 3], [5, 6], [7]]
print(list(flatten(list_num)))
