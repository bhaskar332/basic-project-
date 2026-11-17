#using enumerate
my_list = [21, 22, 24, 53]
for index, val in enumerate(my_list):
    print(index, val)
    
#start the indexing with non zero value
my_list = [21, 22, 53, 43]
for index, val in enumerate(my_list, start= 1):
    print(index, val)
    
#without using enumerate
my_list = [12, 22, 23, 23]
for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)
    
