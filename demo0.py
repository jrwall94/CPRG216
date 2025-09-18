x = 5    #Assignment statement: (int)
         #CPU, allocate a piece of memory, call it x, put the value 3 in it
y = 7.5  #Float
msg = "Hey" #String
name = "Jon"  #String
awake = True  #Boolean
asleep = False #Boolean

print(x) #Function call
print(f"{msg} {name}! {x} plus {y} equals {x+y}.")
print(awake)

print(x, type(x))
print(y, type(y))
print(msg, type(msg))
print(awake, type(awake))

PI = 3.14 # Constant in uppercase (convention)
msg = "bye" # Reassignment

a = 3 + 4 # Operation
area = PI * (x**2)

print("The area of the circle is", area)

print(3 // 4) # floor division
print(4 % 3) # remainder
print(3 ** 3) # power

e = x + y # Process assignment from right to left
# Evaluate x+y first, then assign that value to e
