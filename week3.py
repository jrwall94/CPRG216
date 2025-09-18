# This is our third class demo

'''
In this class we will work on variables, 
operators and other stuff
'''
# Review

# Assignment

x = 5
y = 7.5
name = "Jon"
awake = True

print(x, type(x))
print(y, type(y))
print(name, type(name))
print(awake, type(awake))
print(x+y, type(x+y))
print(type(type(x)))
print(type(print()))

# Some function calls: print, input, int, float, str, bool

num_as_text = "43"
num_as_num = int(num_as_text) # Casting string to int

print(num_as_text) # Will print as text
print(num_as_num + 5) # Prints because python uses str() function behind the scenes

num = 3
num_f = float(3)

num2 = 3.4
num2_i = int(num2)
num2_as_text = str(num2)

print(num2_as_text)