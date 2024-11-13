my_dict = {'Anna': 1997, 'Olga': 2001, 'Igor': 1999}
print(my_dict)
print(my_dict.get('Anna'))
print(my_dict.get('Pavel', 'Ошибка'))
my_dict.update({'Inna': 2000,
            'Piter': 1998})
a = my_dict.pop('Igor')
print(a)
print(my_dict)
my_set = {3,3,5,5,5,4,'d','f','d','f'}
print(my_set)
e2 = (25,1.35)
my_set.update(e2)
print(my_set)
print(my_set.discard(5))
print(my_set)



