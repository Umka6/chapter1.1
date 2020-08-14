# 1 Chapter 1 задание
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
print(a%b)
# 2 задание
print(36%5)
# 3 задание
a = input("enter the word:")
if a == a[::-1]:
    print('Это палиндром')
elif a != a[::-1]:
    print('Это не палиндром')
# 4 задание
a = "I Love Java"
a = a[:7]
print(a+"Python")
# 5 задание
b = input("Enter the word:")
print(b*10)
#  6 задание
c = input("Enter the word:")
c = c[::-1]
print(c)
# 7 задание
num = int(input("Enter the number:"))
for i in range(1,11):
    print(i)
# 8 задание
word = 'You know nothing, John Snow'
print(word[:2]+word[25:])
b = 'hi'
print(b)
a = ""
print("Error")
# 9 задание
num = int(input("Enter the number:"))
print("Выведите предыдущее число"+str(num) + 'is' + str(num-1))
print("Выведите следующее число"+str(num) + 'is' + str(num+1))
# 10 задание

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
print(a > b)
# 11 задание
num = int(input('Введите число: '))
if num > 0:
    print('Число положительное')
elif num < 0:
    print('Число отрицательное')
elif num == 0:
    print('Число не положительное и не отрицательное')
else:
    print('error')