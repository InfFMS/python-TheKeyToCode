# Задача 4: Проверка на четность
# Напишите программу, которая запрашивает у пользователя число и определяет, является ли оно четным или нечетным.
# Пример:
# Ввод: 8
# Вывод: Число 8 четное

n = int(input("Enter number: "))
if(n%2==0):
    print("Number " + str(n) + " is even(четное6)");
else:
    print("Number " + str(n) + " is not add(нечетное)");
