'''
Topic 9 : Strings :
    --> Strings in python are surrounded by either single quotation marks, or double quotation marks
Syntax :
      print("value")
      print('value')
'''
print("Hii")
# Both are valid ways
print('Hii')

# Assign String to a Variable
a = "Good Morning"
print(a)

# Multiline String
    # By using three quotes
s = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(s)

# Three single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


# Strings are Arrays
a = "Hello"
print(a[3])
# Python does not have a character data type, a single character is simply a string with a length of 1


# String Length
    # --> To get the length of a string, use the len() function.
a = "Shyam"
print(len(a))

# Check String
    # --> To check if a certain phrase or character is present in a string, we can use the keyword in
s = "This is a string."
print("string" in s)    #Check if "string" is present in the following text

# Check if NOT
    # --> To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
s = "This is a string."
print("the" not in s)   # Check if "the" is NOT present in the following text