#Write a Python program to read and print values of tuples from console I/OO
t=input()
a = tuple(int(x) for x in t.split())
print(a)