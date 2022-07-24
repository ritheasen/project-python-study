#Function Celcius to Farenheit
def celToFar():
    cel = int(input("Enter weahter in celcius"))
    far = cel * 9/5 + 32
    print(f"Weather in Farenheit: {far}")

celToFar()

#Function Farenheit to Celcius
def farToCel():
    far = int(input("Enter weather in Farenheit : "))
    cel = (far -32) * 5/9
    print(f"Weather in Celcius: {cel}")
farToCel()
