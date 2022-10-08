a = input("Введите предложение: ")
a = a.split()
a = ''.join(a)
print(a)
if a == a[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')






