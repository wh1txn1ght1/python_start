# step one
print("Step one. Пример соединений")
a = "Моё имя "
b = "Александр"
print(a+b)
name = "Alexander"
print(f"Твое имя {name}")

# step two
print("Step two. Формула ИМТ")
weight = int(input("Введи свой вес (кг): "))
height = int(input("Введи свой рост (см): "))
imt = weight/(height/100)**2
imt = round(imt, 1)
print(f"Твой ИМТ равен {imt}")

# step three
print("step three. Математические операции")
print("Введите число")
number = int(input())
print(f"Квадрат числа: {number**2}, Куб числа: {number**3}, Остаток при делении на 7 числа: {number%7}")

# step four
print("step four. Длина слова и символ")
print("Введите слово")
text = str(input())
length = len(text)
print("Длина слова ", length)
if len(text)>3:
    print("Четвертый символ ",text[3])
else:
    print("Слово слишком короткое.")
#step five
print("step five. Итог")
age = int(input("Введи свой возраст: "))
if age<18:
    print("Ты еще подросток")
elif age<40:
    print("Ты взрослый")
else:
    print("Ты старший")