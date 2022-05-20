n = int(input("Enter the number amount of multiply table: ")) # start from 1 until n (input number)
i = 1 #  first number start from 1
while (i <= n): # from i=1 until <= n
    j = 1 # second number start from 1 until <=10
    while(j <= 10): # from j=1 until <=10 (limit)
        print(i , "x" , j , "=" , i * j)
        j = j+1
    i = i+1
    print("\n")
