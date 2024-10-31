n = int(input('Введите число от 3 до 20:'))
def get_password(number):
    password = ''
    for i in range(1, number):
        for k in range(2, number):
            if k <= i:
                continue
            if number % (i + k) == 0:
                password += str(i) + str(k)
    return  password

result = get_password(n)
print('Пароль', result)