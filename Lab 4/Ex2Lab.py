import re

S = input("Enter a string: ")
words = re.findall('^[a-z]+|[A-Z][^A-Z]*', S)

L = [element.lower() for element in words]

print(f"The number of elements is: {len(L)}")
print(f"The string after the split is and lower-case:{L} ")

L.reverse()
print(f"The string after the order change is :{L} ")
