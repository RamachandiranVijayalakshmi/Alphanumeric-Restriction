def string(s):
    if len(s) == 0:
        return False
    if all(['0' <= c <= '9' for c in s]):
        return True
    if all(['a' <= c <= 'z' or 'A' <= c <= 'Z' for c in s]):
        return True
    return False
b=input('Enter the values:')
print(string(b))