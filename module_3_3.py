# 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params('a', 'b', 'c')
print_params(5)
print_params(8, False)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# 2. Распаковка параметров
values_list = [4, 'string', (2, 6, 8)]
values_dict = {'a': 'Love', 'b': True, 'c': 88}
print_params(*values_list)
print_params(**values_dict)

# 3. Распаковка и отдельные параметры
values_list_2 = ['Infinity', 25]
print_params(*values_list_2, 42)
