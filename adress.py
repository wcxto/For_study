# Вводится адрес (каждое значение с новой строки) в формате: город, улица, номер дома (целое число), номер квартиры (целое число). 
# Сформировать строку по шаблону: "г. <город>, ул. <улица>, д. <номер дома>, кв. <номер квартиры>", используя F-строку. 
# Результат вывести на экран.


city = input()
street = input()
house = int(input())
apartment = int(input())

adress = f"г. {city}, ул. {street}, д. {house}, кв. {apartment}"
print(adres)
