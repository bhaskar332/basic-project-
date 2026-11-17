my_list = [ 12, 65, 68, 49, 85, 85, 693, 130]
result = list(filter(lambda x: (x % 13 == 0), my_list))
print("Number divisible by 13 are", result)