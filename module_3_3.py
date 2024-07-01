def print_params(a=1, b='строка', c=True):
    print(a,b,c)
print_params(c=2, b=4)
print_params()
print_params(b=25)
print_params(c=[1,2,3])
walues_list = [15, 'Urban', True]
walues_dict = {'a': 'barbaris', 'b': 4, 'c': False}
print_params(*walues_list)
print_params(**walues_dict)
walues_list_2 = [44.56, 'combat']
print_params(*walues_list_2, 42)