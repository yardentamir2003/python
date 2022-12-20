str_equation = input("Enter equation with this template ax+b=c or ax-b=c: ")
x_index = str_equation.index("x")
equal_index = str_equation.index("=")
a = float(str_equation[:x_index])
b = float(str_equation[x_index+1:equal_index])
c = float(str_equation[equal_index+1:])
x = (c - b) / a
print("x =", x)
