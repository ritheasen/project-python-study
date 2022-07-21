#Functions without arguments and without
def defaultFunction():
    print("Hello I am a function with no arguments and return values")
    print("I will do whatever the task you ask me to do but won't respond you back with return")

defaultFunction()
#Function with argument and without return values

def functionWithTwoArgsButNoReturnValue(name,num_of_times):
    for i in range(0,num_of_times):
        print(name)
    print("I am a function with two paramenters and no return value")

functionWithTwoArgsButNoReturnValue("Thearin",5)

def functionWithNoArgsButReturnValue():
    print("I am a function without any arguments but I will return you a message")
    print("Make sure to store the result on a local variable")
    return "Have a great day ahead!"
messageFromFunction = functionWithNoArgsButReturnValue()
print(messageFromFunction)


#Function
def functionWithTwoArgsAndReturnValue(num1, num2):
    print("I am a function with two arguments and I will return the result")
    sum = num1 + num2
    return f"Sum = ${num1 + num2}"

resultFromFunction = functionWithTwoArgsAndReturnValue(45,65)
print(resultFromFunction)





