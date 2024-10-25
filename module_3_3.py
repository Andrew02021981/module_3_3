#1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(a = 2, b = 'Sun', c = False)
print_params(a = 2, b = 'Sun')
print_params(b = 'Sun', c = False)
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

#2
values_list = [100, 3.14, 'Паганини']
values_dict = {'a':10, 'b':20, 'c':30}

print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = ['Бах', False]

print_params(*values_list_2, 42)


