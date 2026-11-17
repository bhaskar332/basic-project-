#Taking kilometer input from the user
kilometer = float(input("Enter value in kilometer:"))
#conversion factor
conv_fac=0.621371
#calculate miles
miles = kilometer * conv_fac
print('%0.2f kilometer is equal to %0.2f miles' %(kilometer,miles))