print("Сумматор")
number = ("0")
quantity = 0
print("Для прекращения работы введите Y")
while True:
    choise = input("Введите число: ")
    if choise.lower() != "y":
        print(float(number) + float(choise))
        number = float(number) + float(choise)
        quantity = quantity + 1
        average = number / quantity
        print("Среднее арифмитическое =", average)
    else:
        break
print("Работа завершена")