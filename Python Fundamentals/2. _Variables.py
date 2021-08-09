'''
Topic 2 : Create a variable and print the value.
--> The given value will be stored in the variable defined and then the print function will print that value.
Syntax :
        variable_name = value
        print(variable_name)
'''

a = 10   # In python there is no need to specify the datatype it will automatically take as per the value provided
print(a)

# String variables can be declared either by using single or double quotes

n = "Shyam"
# both are same
n = 'Shyam'
print(n)

# Variable names are case-sensitive
x = 12
X = "Hii"
print(x)    #x will not overwrite X


# A variable can have a short name (like a and b) or a more descriptive name (fname, lname, sum, average)
# Rules for Python variables:
    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (name, Name and NAME are three different variables)

# Valid variable names:
var = "Gita"
Var = "Gita"
VAR = "Gita"
vAr = "Gita"
_var = "Gita"
V_ar = "Gita"
Var__ = "Gita"
var1 = "Gita"

# Invalid variable names:
# 1var = "Gita"
# ?var = "Gita"
# $var = "Gita"
# V-ar = "Gita"
# V ar = "Gita"
# .var = "Gita"


# Multi Words Variable Names

variablename = "Hello!!"       # difficult to read the Variable Name

# There are several techniques you can use to make them more readable
    # 1. Camel Case
    # 2. Pascal Case
    # 3. Snake Case

variableName = "Hello"      # Camel Case : Each word, except the first, starts with a capital letter

VariableName = "Hii"        # Pascal Case : Each word starts with a capital letter

variable_name = "Hey!"      # Snake Case : Each word is separated by an underscore character


# Multiple Values to Multiple Variables
    # --> Python allows you to assign values to multiple variables in one line

c1,c2,c3 = "black", "red", "green"
print(c1)
print(c2)
print(c3)


# One Value to Multiple Variables
    # -->   You can assign the same value to multiple variables in one line

v1=v2=v3 = 12
print(v1,v2,v3)     # you can write all the variables separated by (,) using only one print function and it will be printed in a single line


# Output Variables
    # --> The Python print statement is often used to output variables
    # --> To combine both text and a variable, Python uses the + character

x = "Good morning"
print("Hello," +x)      # x will be combined after the given text

x1 = "Hello,"
print(x1, "Good morning")   # Here, x will be combined before the given text
# Where the variable is before some text, there is no need to use + character

# You can also use the + character to add a variable to another variable
a = "How are"
b = " you"
print(a+b)

# If you try to combine a string and a number, Python will give you an error
# x = "ABCD"
# y = 1
# print(x+y)      # TypeError: can only concatenate str (not "int") to str