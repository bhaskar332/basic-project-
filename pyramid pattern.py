#print patter using star
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()
    
#print patter using number
    
rows = int(input("Enter the number of rows:"))
for i in range (rows):
    for j in range(i+1):
         print(j+1, end =" ")
    print()
    
#print pattern using Alphabet

rows = int(input("Enter number of rows: "))
ascii_value = 65
for i in range(rows):
    for j in range (i+1):
        alphabet = chr(ascii_value)
        print(alphabet , end=" ")
    ascii_value +=1
    print()
    
#inverted half pyramid triangle
rows = int(input("Enter the number of rows:"))
for i in range(rows, 0, -1):
    for j in range(0 + i):
        print("* ", end=" ")
    print()
