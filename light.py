# Отсортируйте словарь по значению в порядке возрастания и убывания.
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

result = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(result)
