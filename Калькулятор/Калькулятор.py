from time import sleep

print("Калькулятор\nВот все действия которые есть в нашей программt\n+ - / *\nВведите действие которое мы будем делать:")
action = input()
print("Введите первое число:")
number1 = int(input())
print("Введите второе число:")
number2 = int(input())

for i in action, number1, number2:
    if action == "+":
        answer = number1 + number2
        print(f"Вы сложили числа {number1} + {number2} = {answer}")
        sleep(10)
    elif action == "-":
        answer = number1 - number2
        print(f"Вы вычтели  числа {number1} - {number2} = {answer}")
        sleep(10)
    elif action == "/":
        answer = number1 / number2
        print(f"Вы поделили {number1} / {number2} = {answer}")
        sleep(10)
    elif action == "*":
        answer = number1 * number2
        print(f"Вы умножили числа {number1} * {number2} = {answer}")
        sleep(10)
    else:
        print("Введите правильно значение((")
        sleep(10)

        #Cамый легкий калькулятор для python
