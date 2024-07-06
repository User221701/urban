# Список
my_dict = {'Oleg': 2002, 'Max': 2000, 'Petya': 2005 , 'Masha': 2001}
print(my_dict)
print(my_dict['Oleg'])
# print(my_dict['Pavel']) Вызывает ошибку
print(my_dict.get("Pavel"))
my_dict['Pavel'] = 2001
my_dict['Irina'] = 2004
print(my_dict.pop("Max"))
print(my_dict)
# Множества
my_set ={1,2,2,"Oleg",'hello','hello'}
print(my_set)
my_set.add(2002)
my_set.add(False)
my_set.remove('hello')
print(my_set)
