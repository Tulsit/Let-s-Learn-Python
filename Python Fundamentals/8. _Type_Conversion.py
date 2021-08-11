'''
Topic 8 : Type Conversion : If the user wants to convert one data type to another then it can be done with the int(), float(), and complex() methods
--> Complex data type cannot be converted into any other type.
Syntax :
        variable_name = value
        new_variable_name = data type(variable_name)
        print(new_variable_name)
        print(type(variable_name))
'''

a = 20
a1 = complex(a)     #int to complex
print(a1)
print(type(a1))

b = 92
b1 = float(b)     #int to float
print(b1)
print(type(b1))

c = 3.333
c1 = int(c)     #float to int
print(c1)
print(type(c1))

d = 6.34119
d1 = complex(d)     #float to complex
print(d1)
print(type(d1))

