message = "welcome to KiT"

#conveting all the letters to upper case
print(message.upper())

#converting all the letters to lower case
print(message.lower())

#capitalizing the text
print(message.capitalize())

#casefolding the text
print(message.casefold())

#centering the string
#print(message.center(25,"."))
print(message.center(50))

#finding the index of the searching string (result is the START index)
print(message.find("Kit"))

#True or False based on the existence of the searched string
print("KiT" in message)

#