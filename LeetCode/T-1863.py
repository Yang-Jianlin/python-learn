L = [1, 2, 3]
List = [[]]
for i in range(len(L)):  # 定长
    for j in range(len(List)):  # 变长
        List.append(List[j] + [L[i]])
print('List =', List)
List.pop(0)

result = []
for i in List:
    s = i[0]
    for j in range(1, len(i)):
        s = s ^ i[j]
    result.append(s)

print(sum(result))

