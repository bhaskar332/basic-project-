#Using a temporary variable

x = 5
y = 10
temp = x
x = y
y = temp
print('the value of x after swapping: '.format(x))
print('the value of y after swapping: '.format(y))

#Without using temporary variable

x = 5
y = 10
x, y = y, x
print("x =", x)
print("y =", y)
