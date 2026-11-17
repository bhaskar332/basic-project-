x = [[12,7,3],
     [3,5,9],
     [8,5,2]]

y = [[5,8,1],
     [3,7,5],
     [5,3,8]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range (len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
    for r in result:
        print(r)

## Program to add two matrices using list comprehension

x = [[12,7,3],
     [3,5,9],
     [8,5,2]]

y = [[5,8,1],
     [3,7,5],
     [5,3,8]]

result =[[x[i][j] + y[i][j] for j in range(len (x[0]))] for i in range (len(x))]
for r in result:
    print(r)
