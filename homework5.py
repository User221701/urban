immutable_var = ("Oleg",22,1.5)
print('Immutable tuple:', immutable_var)
#immutable_var[0] = 'Petya'
# Мы не можем изменить immutable_var потому что кортежи неизменяемы. Если вам нужны изменяемые последовательности, используйте списки.
mutable_list = ["Oleg",22,1.5,immutable_var, False]
mutable_list[0] = 'hello'
print('Mutable list:', mutable_list)

