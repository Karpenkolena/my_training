def password(number):
    unique = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                unique += str(i) + str(j)
    return unique

print('Введите число: ')
print(password(int(input())))
