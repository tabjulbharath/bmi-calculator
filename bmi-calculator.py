#!/usr/bin/python3

# get user input, saved as integers
a = int ( input ("weight in kg: ") )
b = int ( input ("height in cm: ") )

# transform cm to meters
c = b/100

# calculate bmi
d = a/ (c*c)

# print results & bmi
print ("you weight", a, "kg and you are ", c, "m tall")
print ("your bmi:", d)
