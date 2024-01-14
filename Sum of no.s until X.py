print("Please enter your numbers to be added. \n\nInput 'x' if you are done with adding your numbers.")
sum = 0
while True:
    i = input("Please enter your values here : ")
    if i == "x":
        print("The sum of your values is : ", sum)
        break
    try:
        i = int(i)
        sum += i
    except ValueError:
        print("Please enter either 'x' or any other number.")