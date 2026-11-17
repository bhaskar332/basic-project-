my_string =  "Python"
print(my_string.strip())

my_string = "\nPython"
print(my_string.strip(""))

#using regular expressions
import re
my_string = "Hello python"
output = re.sub(r'^\s+|\s+$', '', my_string)
print(output)