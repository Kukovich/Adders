print("Сумматор")
number = ("0")
print("Для прекращения работы введите Y")
while True:
    choise = input("Введите число: ")
    if choise != "Y":
        print(float(number) + float(choise))
        number = float(number) + float(choise)
    else:
        break
print("Работа завершена")