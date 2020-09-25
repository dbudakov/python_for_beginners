from sys import argv

# Присвоение значений переменным, переданных аргументов(первый передаваемый имя скрипта)
script, filename = argv

print(f"Я собираюсь стереть файл {filename}.")
print(f"Eсли вы не хотите стирать его, нажмите сочетание клавиш CTRL+C(^C).")
print("Если хотите стереть файл, нажмите клавишу Enter.")

input("?")

# запись в переменную "открытие файла"
print("Открытие файла...")
target = open(filename, 'w')

# открытие файла и его очистка
print("Очистка файла. До свидания!")
target.truncate()

print("Теперь я запрашиваю у вас три строки.")

line1 = input("строка 1: ")
line2 = input("строка 2: ")
line3 = input("строка 3: ")

# запись в файл построчно
print("Это я запишу в файл.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# открытие файла и применеие опции/операции закрытия
print("И наконец, я закрою файл.")
target.close()
