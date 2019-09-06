## find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

s = raw_input()
print(any("True" if s.isalnum() else "False"))
print(any("True" if s.isalpha() else "False"))
print(any("True" if s.isdigit() else "False"))
print(any("True" if s.islower() else "False"))
print(any("True" if s.isupper() else "False"))
