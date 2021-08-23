L = [1, 2, 3]
List = [[]]
for i in range(len(L)):  # 定长
    for j in range(len(List)):  # 变长
        List.append(List[j] + [L[i]])

print('List =', List)
