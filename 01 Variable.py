mark1 = 78
mark2 = 98.5
mark3 = 88.45
result = "true"

firstName = "Vignesh" #camel casing
lastName = "Manoharan"

print(mark1)
print(mark2)
print(mark3)

print(firstName)
print(lastName)
print(firstName + " " + lastName + " : Mark1 " + str(mark1))

#converting a number into a string
strMark = str(mark1)
print(strMark)

#showing type of variable
print(type(mark1))
print(type(strMark))
print(type(mark2))
print(type(result))

result = bool(result)
#print(result) automatic True
print(type(result))