Каждое значение в python имеет `тип`.
В python - всё `объект`,`типы` являются `классами`, а `значения` - экземплярами(объектами) этих классов

#### Объекты

Целые числа(int)
Дробные числа(float)
Строки(str)
Списки(list)
Tайплы(tupl) - Неизменяемые списоки
Словарь(dict) - Внутри находится список соответствия `key`-`value`, где `key` не могут совпадать
Множество(set) - Внутри находятся только `value`, при этом `value` не могут совпадать

#### Операторы вывода

Тип значения(type)
Длинна строки(len)
Representation output(repr)

```py
.add(4) # добавление значения
.append(set_) # добавление например словаря
'{}'.format(set_) # подстановка
```

Переменными для примера служат `spam` и `eggs`

Все переменные должны начинаться с символа или подчеркивания, и могут содержать:

- Латинский алфавит,цифры и нижние подчеркивания
- `snake_case` - переменные в стиле `слово_следуещее_слово`
- Верхний регистр используется для объявления констант

### Вывод типа данных

```py
type(5.5)
type(5)
type(3/2)
```

### Операции над числами и сравнения

```py
// # деление без остатка
%  # остаток от деления, 5%2 будет 2 и 1 в остатке ответ 1
** # возведение в степень
+= # увеличение и присваивание значение
*= # умножение и присваивание значения
```

#### Булевы заначения,сравнения

```py
== # равно
!= # не равно
>= # больше или равно
```

#### Пример

Работа с переменными, вычисление площади прямоугольника

```py
  side_a = 5
  side_b = 7
  s = side_a * side_b
  p = side_a * 2 + side_b * 2
```

`spam` и `eggs` - переменные используемые для примера

```py
spam = 40
spam = spam + 1 # увеличивает значение на 1
spam += 1 # также увеличивает значение на 1
spam -= 2 # уменьшает и записывает spam на 2
spam *= 3 # умножает и записывает заначение spam на 3
spam /= 4 # делит и записывает значение spam на 4
```

### СТРОКИ

для объявления строк используются как одинарные так и двойные кавычки
для многострочных текстов используется по три кавычки вначале и в конце - либо одинарные, либо двойные. Внутри можно использовать такие же кавычки

проверим и изменим тип переменной `spam`

```py
type(spam)
# float

spam = "eggs"
type(spam)
# str

spam = "'some text'"
spam
# 'some text'

print(spam)
# some text

spam = 'some \' text'
spam
# 'some ' text'

spam = 'some\ntext' # new line
spam
print(spam)

spam = '''  # inser text list
some
text
line
'''
print(spam)

'spam' * 3
'spam' + 'eggs'
'spam' / 4 <TypeError> # as spam it string(str) `spam` can't divide
```

### ИНДЕКСЫ

Чтобы получить конкретный символ из строки нужно использовать индексы, индексирование в phyton начинается с нулевого элемента

```py
  +---+---+---+---+---+---+
  | q | w | e | r | t | y |
  +---+---+---+---+---+---+
  0   1   2   3   4   5   6
 -6  -5  -4  -3  -2  -1

  some_str = "qwerty"
  some_str[0]   # первый элемент
  some_str[-1]  # последний элемент
  some_str[1:4] # то что между индексами 1 и 4
  some_str[:4]  # с начала и до 3 символа
```

#### Длинна строки

```py
  spam = "abcde"
  len(spam)
  spam[5]
  or spam[len(spam) - 1]
  or spam[-1]
  spam[-2:-1] # show last 2 symbol
  spam[-1:-2] # empty output
```

### СПИСОК

Список - это упорядоченный массив объектов (подобно локомотиву где вагоны идут один за другим)

Создадим массив

```py
array = [1, 2, 3, 4, 5]
len(array) # вернет 5
array[0] # вывод первого элемента
array[3:4] # в выводе будет только третий элемент, четвертый элемент не включается
array[0] = 10
array[:2] = [6, 7, 8] # кроме значений измениться и длина
len(array)

array.append(11) # добавление в конец
array += [2]  # добавление 2 в конец списка, здесь [2] список из одного элемента
array.inser(0, 4) # вставка 4 в нулевой индекc , остальные сдвигаются
array.pop() # по умолчанию забирает последний элемент
array.pop(1) # вырезает значение под индексом [1], двигая остальные элементы
```

Создадим tuple(неизменяемый) массив

```py
tpl = (7, 6, 5)
type(tpl) # tuple
tpl[2] = 7 # TypeError

```

### СЛОВАРЬ(dict)

```py
dct = {'key':'value'} # key не может быть однинаковым, value - может
type(dct) # вывод типа объекта(dict)
type({})
dct['spam'] = 'eggs' # создание ключа spam и соответствующего ему значения eggs
dct
dct.keys() # вывод всех ключей(key) dct
dct.values() # вывод всех значений(value) dct
dct.items() # вывод всех объектов словаря
dct['spam'] # вывод значения записанного под ключем spam
dct['spam'] = dct['spam'] * 2 # изменение записи

```

### МНОЖЕСТВО(set)

`list` и `set` являются изменяемыми типами данных, но в `set` нельзя добавить `list` так как `list` нехешируемый, а в `list` добавить `set` можно

```py
set_ = {1, 2, 3}
set()
type(set()) #  <class 'set'>
set_.add(4)

# Добавление `set_` к `array`
array.append(set_)
array

# В случае если set_ меняется меняется и состав array
set_.add(5)
array

# Запись в `set_`, через `array` элементом которого является `set_`
array[-1].add(6) # `set_` изменится
```

#### Форматирование строк

```py
# Нельзя добавлять int к str
'some text: ' + 42 # TypeError

# добавление возможно только строка к строке
'some text: ' + str(42)

str(42) # строка(str)
42 # целое число(int)
```

показать список в строке

```py
# в %s вставятся значения указанные после знака %
'our list: %s' % array # вставит список array вместо %s
'a: %s, b: %s' % (42, 'spam') # на место первой %s уйдет 42, на место второй spam
```

#### Экранирование %

```py
repr('spam') # будут выводиться кавычки, чтобы мы понимали что это строка
'repr: %r' % 'spam'
'%s %%s' % 42 # экронирование процента
```

### Формулы

```py
# подстановка
set_ = {1, 2, 3, 4}
'our set: {}qwerty'.format(set_) # 'our set: {1, 2, 3, 4}qwerty'
'value: {}'.format(42)
'value {{ {} }}'.format(set_)
'our list {{ {}'.format(array)
'{}{}'.format(10, 20) # output 1020

# подстановка по индексам
'{1} and {0}'.format('eggs','spam') # вывод 'spam and eggs 00:42:10
'{0}{1}{0}'.format(13,11) # еще одна подстановка по индексам

# подстановка по значениям
'{value}{key}{value}'.format(value=42, key='spam')

# вывод в виде representation
  '{!r}'.format('spam and eggs')

# округление до сотых
'value: %.2f' % 12.345
# .2f - означает что тип float округляется до двух символов после запятой, 4'ка округлиться до 5, 5'ка уйдет
'value: {:.2f}'.format(34.321)
```

## f строки

```py
array = [1, 2, 3, 4, 5]
f'value {array}' # подставиться array

# все что внутри круглых строк склеится и будет одна строка текс,
# нельзя использовать запятые, так как это станет типом tuple
value = 123.456
a_line = 'spam and eggs'
text = (
    'first line'
    f'\na value {value:.2f}'
    f'\na line {a_line!r}'
)
print(text)
```

### Списки внутри списков

```py
# Три списка, к которым можно обратиться по индексу
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
matrix[0] # выведеть список под индексом [0]
matrix[1][2] # выведет заначени под индексом  [2] из списка с индексом [1]
```

### Операторы ветвления

При помощи оператора ветвлелния происходит выбор действия, которое необходимо выполнить, в зависимости от условия на момент проверки условия в python этими операторами являются `if` и `else`
Проверить условие и записать значение в переменную

```py
a=5
b=6
if a > b:
    value = a * 2
else:
    value = b // 2
print('Value is', value)

# var.2
value = a * 2 if a > b else b // 2 # a*2 если a>b в ином случае b/2
print('Value is', value)
```