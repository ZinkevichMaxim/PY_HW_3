# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

# list_1 = [1, 2, 3, 4, 5]
# k = 3


n = int(input('Введите длину массива \n'))
list_1 = []
for i in range(n):
    x = int(input('Введите очередной элемент \n'))
    list_1.append(x)
print(list_1)

k = int(input('Введите искомое число \n'))
count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count = count + 1
print(f'Число {k} встречается в списке {count} раз')

