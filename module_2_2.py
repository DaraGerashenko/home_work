from platform import android_ver

#Ввод в консоль 1:123,456,789
#Ввод в консоль 2:42,69,42

print('Введите 3 произвольных числа для сравление')
first = int(input('Введите первоое произвольное число:'))
second = int(input('Введите второе произвольное число:'))
third = int(input('Введите третье произвольное число:'))
if first == second and first == third and second == third:
    print(3) #Если все числа равны между собой, то вывести 3
elif first == second or first == third or second == third:
    print(2) #Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
else:
    print(0) #Если среди чисел нет равных 3-х, вывести на экран значение 0


