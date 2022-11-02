print("Добро пожаловать в простейший калькулятор Python\n"
      "В этом калькуляторе доступны такие операции, как:\n"
      "1 + : Сложение\n"
      "2 - : Вычитание\n"
      "3 * : Умножение\n"
      "4  / : Деление\n"
      "5 ** : Возведение в степень\n"
      "Чтобы выйти из программы, везде введите 0\n")
operation = int(input())
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
def my_sum(a,b):
      return a+b
def my_sub(a,b):
      return a-b
def my_mult(a,b):
      return a*b
def my_div(a,b):
      return a/b
def my_exp(a,b):
      return a**b
if operation == 1:
    print (my_sum(a,b))
elif operation == 2:
    print (my_sub(a,b))
elif operation == 3:
    print(my_mult(a,b))
elif operation == 4:
    try:
        print(my_div(a,b))
    except ZeroDivisionError:
        print('Деление на ноль')
else:
    print(my_exp(a,b))
if operation == 0:
    print('Выход из программы')
