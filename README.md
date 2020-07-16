# Alphanumeric Restriction
- **Create a function that returns True if the given string has any of the following:**
    - **Only letters and no numbers.**
    - **Only numbers and no letters.**
- **If a string has both numbers and letters, or contains characters which don't fit into any category, return False**
- **Any string that contains spaces or is empty should return False.**
## Sample code for alphanumeric restriction
```
if len(s) == 0:
   return False
if all(['0' <= c <= '9' for c in s]):
   return True
if all(['a' <= c <= 'z' or 'A' <= c <= 'Z' for c in s]):
   return True
return False
```
## Example output
```
Enter the values:viji12
False
```
