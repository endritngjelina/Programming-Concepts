'''
Exercise 32: Sort 3 Integers
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
'''
a = int(input('Enter an integer: '))
b= int(input('Enter another integer: '))
c= int(input('Enter the last integer: '))

f = [a, b, c]

mi=min(a, b, c)
ma=max(a, b, c)

md= a + b + c - mi - ma

f.sort()
print(f)

print( mi, md, ma)
