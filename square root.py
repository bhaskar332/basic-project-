#for positive number
num = 8
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

#for complex and real number

import cmath
num = 1+2j
num_sqrt = cmath.sqrt(num)
print('the square root of {0} is {1:0.3f}+{2:0.3f}j' .format(num, num_sqrt.real, num_sqrt.imag))