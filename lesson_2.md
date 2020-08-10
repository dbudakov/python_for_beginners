логические операторы(add,mul) [link](https://docs.python.org/3/library/operator.html)

Метод отличается от функции тем что метод принадлежит классу, а функция она просто функция(напр hash) и не принадлежит классу

range
enumerate
end
continue
yield
fun(seq) - последовательность
fun(start) - начальное значение
Рекурсия
lambda
map - выполняет действие для каждого элемента `values`
filter
from / import
reduce - позволяет произвести операции со всеми объектами из списка
decorator
gen_dec
wraps
contextmanager

```py
# проверка на условие, операторы `and` `or`
a = 16
b = 42
a > 0 and b > 0 # True

b = -1
a > 0 and b > 0 # False
a > 0 or b > 0 # True
```

```py
# Проверка на вхождение, оператор `in`
t = (1, 2, 3, 'abc', 'spam', 'eggs')
5 in t # False
'spam' in t # True
1 in t # True

# Аналогично со списком
'a' in  ['a', 'b', 'c'] # True

# Аналогично со словарем
'key' in {'key': 'value'} # True

# Аналогично для set
7 in {7, 8, 9} # True
```

```py
#
a = 42
if a < 0:
  print('a < 0')
elif a < 10:
  print('0 <= a < 10')
elif a < 100:
  print('10-100')
elif a < 1000
  print('100-1000')
else:
  print('>= 1000')
```

```py
# for интерпритируется по объектам внутри объекта который передан
l = [0, 1, 2, 3, 4]
for item in l:
    print(item)

# вывод будет в порядке возрастания
for s in {5, 3, 8, 2, 22}:
  print(s)

```

```py
hash(42) # output 42
```

```py
dct = {'key': 'value', 'spam': 'eggs'}
for key in dct:
    print(key, dct[key])

# var1 show only values
for values in dct.values():
    print(values)

# var.2 show only values
dct.values() # dict.values(['value', 'eggs'])
```

```py списки
results = []
values  = [1, 2, 3, 4, 5]
for value in values:
    relusts.append(value ** 2)
print(results) # [1, 4, 9, 16, 25]
```

```py
# вывод строки значения которой разделены пробелом
for c in 'abcdefg':
    print(c, end=' ') # a b c d e f g
```

```py
# склеить в строку все значения
strings = ['abc', 'def', 'ghi']
for s in strings:
    strings += s
print(strings) # abcdefghi

# без использования for
''.join(strings)  # 'abcdefghi'
' '.join(stings)  # 'abc def ghi'
', '.join(stings) # 'abc, def, ghi'

# возведение в квадрат всех значений из list,set,disct values
[val ** 2 for val in values]
{val ** 2 for val in values}      # {1, 4, 9, 16, 25}
{val: val ** 2 for val in values} # {1: 1, 2: 4, 3: 5, 4: 16, 5: 25}
```

# Генератор

```py
# Генератор похож на итератор но данные из него можно прочитать только единожды, связано с тем что генератор создает значения на лету, в тот момент когда мы к нему обращаемся, он не помнит предыдущее значение, еще не знает о следующем значении, он возвращает значение для этого этапа
(val ** 2 for val in values) ## <generator object <genexpr> at ***>

gen = (val ** 2 for val in values)
next(gen)  # 1; каждое обращение следующий шаг
next(gen)  # 4;
list(gen)  # [9, 16,25]; конвертиция генератора в список
```

```py
# в данном примере используется срез [:], без него программа войдет в цикл, прогоняя заново все значения
lines = ['spam', 'eggs', 'another line']
for line in lines[:]:
    if len(line) > 7: # если длина текущей строки больше 7
        lines.insert(0, line) # то продублировать строку
lines
```

Вывод каждого второго элемента

```py
# передаем шаг для выборки из полного списка
line = 'python'
line[::2]

# можно развернуть(инвертировать) список
values[::-1]
line[::-1]
```

```py
range(10) # range(0, 10)
list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(7, 13)) # [7, 8, 9, 10, 11, 12]

# установка range от 10 до 40 с шагом 3
list(range(10, 40, 3)) # [10, 13, 16, 19, 22, 25, 28, 31, 34, 37]

# range в цикле for
for i in range(5):
    print(i)

# возведение в степень с помощью range
for i in range(1, 5):
    print(i, '^2', i ** 2)
```

```py
# вывод списка соответствия индекса значению
values = list(range(7, 13))
values # [7, 8, 9, 10, 11, 12]
for i in range(len(values)):
    print(i, values[i])
```

```py
a = 16
b = 42
a, b # 16, 42
x, y = a, b
x # 16
y # 42
a, b = b, a
a, b # 42, 16
```

```py
# enumerate возвращает пары где первое это индекс , а второе это значение из переданного внутрь объекта
enumerate(range(10))

e = enumerate(values)
next(e)
next(e)
next(e)
list(e)

# вывод индекса и соответствующего ему значения
values = [7, 8, 9, 10, 11, 12]
for i, val in enumerate(values):
    print(i, val)

# передать начальное значение, для нумерации не с 0
values = [7, 8, 9, 10, 11, 12]
for i, val in enumerate(values, 1):
    print(i, val)
```

#### break and else

```py
# `else` выполняется после прогона `for`
for i in range(5):
    print(i)
else:
    print('else!')

# оператор `break` прекращает выполнения цикла
for i in range(10, 100, 5):
    print(i)
    if i >= 30:
        break
```

### оператор while

```py
while True:
    print('Once')
    break
```

```py
# var1 простой счётчик
i = 0
while True:
    print(i)
    i += 1
    if i > 3:
      break
else:
    print('Else!')

# var2
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('Else!')
```

Выводим четное или нечетное число

```py
# проверка на четность осуществляется делением на 2 и сравнением остатка с 0, т.е. деление на 2 без остатка
# операция i % 2 - выводит остаток после деления на 2
for i in range(1,5):
    print(i, end= ' is ')
    if i % 2 == 0:
        print ('even')
    else:
        print ('odd')
```

```py
# после continue, операции не выполняются
for i in range(1, 8):
    print(i)
    if i % 2 == 0:
        print('is even')
        continue
        print('never printed')
    print('is odd ')
```

### Функции

```py
def some_function():
    pass


some_function()
```

```py
def some_function():
    print('Hello world!')

some_function()
```

```py
# phython всегда что-то возвращает, либо возвращает специальный объект ничто
print(None, type(None))
```

```py
# возврат значения
def return_2():
    return 2

return_2() # 2
```

```py
# ввод и возврат функции
def out_fun():
    def inner():
        return 'inner text'
    return inner

out_fun() # вернет inner()
# повторный вызов функции

# var1
out_fun()() # вернет 'inner text'

# var2
fun = out_fun()
fun() # вернет inner text
```

### область видимости

```py
def out_fun():
    def inner():
        return 'inner text'
    return inner


inner() # NameError, так как inner задана внутри другой функции
```

#### Ввод переменной в функцию

```py
def mul_x(x):
    print('Got', x)
    return

mul_x() # NameError
mul_x(3) # Got 3
```

```py
def mul_x(x):
    print('Got', x)
    def multiply(y):
        return x * y
    return multiply

# var1
mul_3 = mul_x(3)
mul_3
mul_3(5) # 15

#var2
mul_x(3)(5)
```

```py
x = 5
def fun1():
    print('1x', x)

def fun2():
    x = 10
    print('2x', x)

def fun3():
    x = 15
    print('3x', x)

print(x)


fun1()
fun2()
fun3()


x = 42
fun1()
fun2()
fun3()
```

```py
def func():
    return (42, 'spam')
func()
a, b = func()
print(a, b)

def func():
    return 42, 'spam', 'eggs'

func()
a = func()
a
```

```py 00:50:00
# `yield` возвращает значение как и `return` только это генератор
def gen():
    yield 42

gen()

g = gen()
next(g)
next(g) # StomIteration
```

```py
# примеры применения yield

def gen():
    for i in range(3):
        return i

gen() # 0, в выводе всегда 0
```

```py
def gen():
    for i in range(3):
        yield i

g = gen()
next(g) # 0
next(g) # 1
next(g) # 2 , конец генератора
list(g) # []
```

```py
#var1,
values = [7, 8, 9, 10, 11, 12]
def our_enum(seq): # внутрь передается последовательность seq-sequence
    n = 0 # создаем итератор
    for item in seq:
        yield n, item
        n += 1 # инкрементируем переменную на 1


g = our_enum(values)
# list уже будет из tuple, каждый tuple индекс и значение values
list(g)

# var2, индекс будет начинать не с 0 а с 1
values = [7, 8, 9, 10, 11, 12]
def our_enum(seq, start):
    n = start
    for item in seq:
        yield n, item
        n += 1
g = our_enum(values, 1)
list(g)

# var3, с указанием дефолного индекса и его переназначением
values = [7, 8, 9, 10, 11, 12]
def our_enum(seq, start=0):
    n = start
    for item in seq:
        yield n, item
        n += 1


list(our_enum(values))
list(our_enum(values, 3))
```

```py
# цикл для чисел фибоначи
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
      result,append(a)
      a, b = b, a + b # сначала складывается ноль, затем 'b' переходит в 'a', в свою очередь 'b' становиться суммой чисел
    return result


fib(100)
```

### Рекурсия

Рекурсия это когда функция возвращает саму себя, точнее результат выполнения от самой себя

```py
# предположение что просчитываются все `n`
def recur_fib(n):
    if n <= 1:
        return n
    return recur_fib(n - 1) + recur_fib(n - 2)

recur_fib(10)
recur_fib(36)
```

```py
def exp(x):
    return lambda y: y ** x


# var1
exp_3 = exp(3)
exp_3(2)
exp_3(4)

# var2
exp(x)(y)
```

```py
# var1
#  генератор выдает сразу номера от 5..9
def gen():
    for i in range(10):
        print(i)
        if i < 5:
            yield 101

g = gen()
next(g)
list(g)

# var2,
def gen():
    for i in range(10):
        print(i)
        if i > 5:
            return
        yield i

g = gen()
```

```py
# выполняет действие для каждого элемента values
values = range(5,8)
mapped = map(lambda x: x + 3, values)
list(mapped) # [8, 9, 10]
list(mapped) # [], так как генератор пустой повторный вывод будет пуст
```

```py 01:09:00
a = 2
def exp(x):
    return lambda y: y ** x

funcs = (exp(x) for x in range(2,6))
# здесь x принимается не число а функция, `a` задана в начале
list(map(lambda f: f(a), funcs))
```

### Фильтры

```py
my_nums = range(-10, 20, 3)
list(filter(lambda x: -7 < x < 10, my_nums)) # -4, -1, 2, 5, 8
```

```py
# import(импорт) операции, reduce(может перемножить все значения из списка)
# reduce аккумулирует результат какого-то действия на список
# например перемножить все значения из списка
from functools import reduce
reduce

# var1
to_mul = range(1, 7)
product = reduce(lambda x, y: x * y, to_mul)
product # 720, результат умножения

# var2
reduce(lambda x, y: x * y, to_mul)

# домножить еще на 10
to_mul = range(1, 7)
product = reduce(lambda x, y: x * y, to_mul, 10)
product # 7200, результат умножения
```

### Декоратор

```py
def a_func():
    print('Hello from a func!')

a_func()

print('some text')
a_func()
```

```py
# var1, создание декоратора для функции
def a_func():
    print('Hello from a func!')

def decorator(func):
    # вводится функция wrapper, которая возвращает значение для декоратора.
    def wrapper():
        print('some text')
        func()
    return wrapper

a_func = decorator(a_func)
a_func()

# var2,  навешивание декоратора
@decorator
def another_func():
    print('another func')

another_func()
```

```py
# передача данных в функцию, которая декорирована
def decorator(func):
    def wrapper(x, y):
        print(x, y)
        return func(x, y) # возвращаем функцию
    return # возвращаем wrapper

@decorator
def count(a, b):
    return a + b

count(3,4)
```

```py
# предыдущий пример через `args`
def decorator(func):
    def wrapper(*args):
        print(args)
        return func(*args) # * означает распаковку по принципу работы `for` и возвращаем функцию
    return # возвращаем wrapper

@decorator
def count(a, b):
    return a + b

count(3,4)
```

```py
# пример с именованным аргументом
def decorator(func):
    def wrapper(*args, **kwargs): # args - аргументы(4, 7), kwargs - именованные аргументы(a = 7)
        print(args)
        print(kwargs)
        return func(*args, **kwargs) # возвращаем функцию
    return # возвращаем wrapper

@decorator
def count(a, b):
    return a + b

count(a=3, b=4)
```

```py 01:21:00
# генератор декораторов
def gen_dec(x):
    print('IN a gen dec')
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        print('Generated a wrapper')
        return wrapper
    print('Generated a decorator')
    return decorator

@gen_dec(42)
def mul(a, b):
    return a * b

mul(3, 4) # 13
```

```py 01:24:30
# использование декораторов, изменяем строку @gen_dec и return под wrapper, в результате домножаем результат на 3
def gen_dec(x):
    print('IN a gen dec')
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(*args, **kwargs)
            return x* func(*args, **kwargs)
        print('Generated a wrapper')
        return wrapper
    print('Generated a decorator')
    return decorator


@gen_dec(3)
def mul(a, b):
    return a * b

mul(3, 4) # 36
```

```py 01:25:00
# еще прием, z берется из подстановки в func()
def gen_dec(x):
    print('IN a gen dec')
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(args, kwargs)
            return func(x, *args, **kwargs)
        print('Generated a wrapper')
        return wrapper
    print('Generated a decorator')
    return decorator


@gen_dec(50)
def mul(z, a, b):
    print(z, a, b)
    return z + a * b

mul(3, 4)
mul # вызов для следующего примера
```

```py 01:26:00
# при вызове mul без скобок будет указано что это wrapper, что плохо для логов
# оформление в правилах хорошего тона, добавляется строка @wraps(func) и тогда на wrapper применяются значения которые имеет исходная функция
def gen_dec(x):
    print('IN a gen dec')
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(args, kwargs)
            return func(x, *args, **kwargs)
        print('Generated a wrapper')
        return wrapper
    print('Generated a decorator')
    return decorator


@gen_dec(50)
def mul(z, a, b):
    print(z, a, b)
    return z + a * b

mul(3, 4)
mul
```

```py 01:27:00
# создание функции которая будет работать с контекстным менеджером
# результат мы получаем внутрь 1, 2, 3  как позиционные аргументы, затем мы получили 42 и сложили с 100 и получили 142, потому что в res  у нас значение которое отдает yield, перед выходом идет вывод Leaving, затем благодаря контекстному менеджеру выполняется  вывод Closed, и затем Left
from contextlib import contextmanager
@contextmanager
def managed_res(*args, **kwargs):
    print(args, kwargs)
    yield 42 # отдает значение в виде генератора
    print('Closed')

with managed_res(1, 2, 3) as res:
    print(res, res + 100)
    print('Leaving')

print('Left')

```

```py 01:30:20
# Для примера представим что в args должно передаваться какое-то кол-во чисел и мы будем из умножать, для этого используем `map`
from contextlib import contextmanager
@contextmanager
def managed_res(*args, **kwargs):
    print(args)
    yield map(lambda x: x * 2, args) # отдает значение
    print('Closed', args)

with managed_res(1, 2, 3) as g:
    print(list(g))
    print('Leaving')
print('Left')

```
