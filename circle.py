# Print the circumference and the area of the circle
# Assume the circle radius is 5, and pi is 3.14

radius = int(input("Enter the radius of the circle:\n>"))
PI = 3.14159265359

circumference = 2 * PI * radius
area = PI * (radius**2)

print(f"The circumference of the circle is: {circumference:.1f}")
print(f"The area of the circle is: {area:.1f}")