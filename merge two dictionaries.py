#add dictionaries using operator
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {3: 'c', 4: 'd'}

print(dict_1 | dict_2)

#add dictionaries using ** operator

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {3: 'c', 4: 'd'}

print({**dict_1, **dict_2})

#add dictionary using copy() and update()

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {3: 'c', 4: 'd'}

dict_3 = dict_2.copy()
dict_3.update(dict_1)
print(dict_3)