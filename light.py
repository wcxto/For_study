# Отсортируйте словарь по значению в порядке возрастания и убывания.
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

result = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(result)

# Напишите программу для слияния нескольких словарей в один.
dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}

result = {}
for d in (dict_a,dict_b,dict_c):
    result.update(d)

result = {**dict_a, **dict_a, **dict_c}
print(result)


a = [-5, -3, 1, 2, 3]
new_a = sorted([i**2 for i in a])
print(new_a)

a = [-5, -3, 1, 2, 3]
print(*a)


date_info = {'year': "2020", 'month': "01", 'day': "01"}
filename = "{year}-{month}-{day}.txt".format(**date_info)
print(filename)

def transpose_list(list_of_lists):
    return [list(row) for row in zip(*list_of_lists)]


print(transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
