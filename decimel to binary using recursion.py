def converToBinary(n):
    if n > 1:
        converToBinary(n//2)
    print(n % 2, end = '')
dec = 6
converToBinary(dec)
print()