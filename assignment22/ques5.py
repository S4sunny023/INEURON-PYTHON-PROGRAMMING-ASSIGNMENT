'''Question5
Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.
Examples
is_in_order("abc") ➞ True

is_in_order("edabit") ➞ False

is_in_order("123") ➞ True

is_in_order("xyzz") ➞ True
Notes
You don't have to handle empty strings.'''

def is_in_order(string):
    return list(string) == sorted(string)

print(is_in_order("abc"))
print(is_in_order("edabit"))
print(is_in_order("123"))
print(is_in_order("xyzz"))
