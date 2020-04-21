#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
#for i in range(6):
#    i=i+1
#    if i==6: break
#    print(i, 'строка: ', 0)

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
#print('Задача 2')
#five = 0
#for i in range(10):
#    answer = int(input('Введите любую цифру: '))
#    if answer == 5:
#        five += 1
#
#print('Количество цифр 5 равно', five)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
#sum = 0
#
#for i in range(1,101):
#    sum+=i
#print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
#mult = 1
#
#for i in range(1,11):
#    mult*=i
#    print(mult)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
#integer_number = 2129

#print(integer_number%10,integer_number//10)
#
#while integer_number>0:
#    print(integer_number%10)
#    integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
#x=int(input('Input number'))
#sum=0
#while x>0:
#    sum += x%10
#    x//=10
#print(sum)


'''
Задача 7
Найти произведение цифр числа.
'''
#x=int(input('Input number'))
#mult=2
#while x>0:
#    mult *= x%10
#    x//=10
#print(mult)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
#integer_number = 213413
#while integer_number>0:
#    if integer_number%10 == 5:
#        print('Yes')
#        break
#    integer_number = integer_number//10
#else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
#n = int(input('Введите число'))
#y = 0
#max = 0
#while n > 0:
#    last = n%10
#    y = y + 1
#    if last > max:
#        max = last
#    n = n // 10
#print('Mаксимальная цифра ', max )

'''
Задача 10
Найти количество цифр 5 в числе
'''
n = int(input('Введите число'))
y = 0
while n >0:
    last = n % 10
    if last == 5 :
        y = y + 1
    n = n // 10
print('Количество цифр 5 равно ', y)
