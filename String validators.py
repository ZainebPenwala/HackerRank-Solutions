''' ANY() keyword = Returns true if any of the items is True. It returns False if empty or all are false. Any can be thought of as a 
sequence of OR operations on the provided iterables.It short circuit the execution i.e. stop the execution as soon as the result is 
known.'''

## find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

s = raw_input()
print(any("True" if s.isalnum() else "False"))
print(any("True" if s.isalpha() else "False"))
print(any("True" if s.isdigit() else "False"))
print(any("True" if s.islower() else "False"))
print(any("True" if s.isupper() else "False"))
