print("What operation would you like?")
op = int(input("\n \n \n 1} Addition \n 2} Subtration \n 3} Multiplication \n 4} Division\n \nEnter 0 to Exit\n \nInput : "))
def ask():
    print("What operation would you like?")
    op = int(input("\n \n \n 1} Addition \n 2} Subtration \n 3} Multiplication \n 4} Division\n \nEnter 0 to Exit\n \nInput : "))
if op==0:
    print("\nEXITING")
elif op==1 or op==2 or op==3 or op==4:
    while op != 0:
        amount = int(input("How many numbers you want to operate on?\n\nInput : "))
        values = []
        for i in range(amount):
            value = float(input(f"\nEnter the {i+1} value : "))
            values.append(value)
        result = 0
        for x in values:
            if op == 1:
                result += x
            elif op == 2:
                result -= x
            elif op == 3:
                result *= x
            elif op == 4:
                result /= x
            print("\nAnswer : ", result)
            print("---\n\n\n")
            print("~~~ Taking you back to main menu ~~~\n\n")
            ask()
else:
    print("INVALID OPERATION")
ask()
