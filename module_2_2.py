first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
third = int(input("Введите третье целое число: "))


if first == second == third:
    print(3)

elif first != second and second != third:
    print(0)

else:
    print(2)
