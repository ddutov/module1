immutable_var = ([1, 2], 55, 'world', True, 36.6)
print(immutable_var)
#immutable_var[1] = 66 #объект 'tuple' является неизменяемым, невозможно изменить элемент кортежа
#print(immutable_var)
mutable_list = [[1, 2], 55, 'world', True, 36.6]
mutable_list[3] = False
add_list = [0, 'list']
mutable_list1 = mutable_list + add_list
print(mutable_list1)