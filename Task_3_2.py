# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 5]
k = 6
min = abs(k - list_1[0])                        # 5       2
index = 0
count = 0
for i in range(len(list_1)):
    count = abs(k - list_1[i])                 # 5 4 3 2 1     2 1 0 -1 -2
    if count < min:
        min = count                       # min =           1 0  -1 
        index = i                                       #  0 1 2  3
print(list_1[index])
