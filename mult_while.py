# На вход программе подается натуральное число (то есть, целое положительное) от трехзначного и более. 
# Необходимо прочитать это число и найти произведение всех его цифр. Результат (произведение) вывести на экран. 
# Программу реализовать при помощи цикла while.


n = input()

res = 1
i=0
while i != len(n):
    res *= int(n[i])
    i+=1
    
print(res)
