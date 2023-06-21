str1="this is string practice tutorial"

# printing length of string
print(len(str1))

# string slicing
print(str1[3:20])
print(str1[3:20:2])
print(str1[-3:-20:-1])
print(str1[-3:-20:-2])

# string operations
str2='hello'
str3='world'

print(str2+str3)
print(str2*2)
print(str2*3)
print(str2*2+str3*3)

print("he" in str2)
print("he" in str3)

# built-in functions
print(str1.find("is",0,16))
print(str1.find("is",10,len(str1)))

str4=str1.replace("tutorial","file")
print(str1)
print(str4)

print("hello".upper())
print("World".lower())