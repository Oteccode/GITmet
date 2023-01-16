from time import sleep

#Здрасте дорогие мои детки конфетки, вот легкий калькулятор на python.
# Калькулятор только по целым числам, Вещественные не работают
print("Введите первое число:")
number1 = int(input())

while not(number1 == -1000000000000000):
    print("")
    print("Введите какое действие будите делать\nСложение --> ( + )\nВычитание --> ( - )\nУмножение --> ( * )\nДеление --> ( / )")
    action = input()
    print("")
    print("Введите второе число:")
    number2 = int(input())
    if action == "+":
        answer = number1 + number2
        print(f"Вы сложили числа {number1} + {number2} = {answer}")
        sleep(5)
    elif action == "-":
        answer = number1 - number2
        print(f"Вы вычтели  числа {number1} - {number2} = {answer}")
        sleep(5)
    elif action == "/":
        answer = number1 / number2
        print(f"Вы поделили {number1} / {number2} = {answer}")
        sleep(5)
    elif action == "*":
        answer = number1 * number2
        print(f"Вы умножили числа {number1} * {number2} = {answer}")
        sleep(5)
    else:
        print("Введите правильно значение((")
        sleep(5)

        #Cамый легкий калькулятор для python
