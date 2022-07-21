f = open("userdetails.text","r")

#d.read() will read the netire details from the file
#f.readline() will read a line from the file
# print(f.read())
# print(f.readline())

print(f"Username: {f.readline()}Password: {f.readline()}")