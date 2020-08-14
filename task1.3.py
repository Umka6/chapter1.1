
a = input("enter the word:")
if a == a[::-1]:
    print('Это палиндром')
elif a != a[::-1]:
    print('Это не палиндром')
