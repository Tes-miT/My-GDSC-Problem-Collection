num = int(input("Please enter your desired number : "))
if num == 0:
    print("Infinite number of factors")
else:
    for i in range(1,num+1):
        if (num % i) == 0:
            print(i, "is a factor of", num)