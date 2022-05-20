number = int(input("Input a number"))
i = 0
num_str = ""

while number>0:
    i = int(number %10)
    number = number//10
    num_str += str(i)

print(num_str)