a = int(input("Please enter the 1st number : "))
b = int(input("Please enter the 2nd number : "))
if a>b:
    big = a
    small = b
    for i in range(small,0,-1):
        if big % i == 0 and small % i == 0:
            print("HCF of the 2 numbers is : ", i)
            break
    for j in range(big,a*b+1):
        if j % small == 0 and j % big == 0:
            print("LCM of the 2 numbers is : ", j)
            break
        else:
            continue
elif a<b:
    big = b
    small = a
    for i in range(small,0,-1):
        if big % i == 0 and small % i == 0:
            print("HCF of the 2 numbers is : ", i)
            break
        else:
            continue
    for j in range(big-1,a*b+1):
        if j % small == 0 and j % big == 0:
            print("LCM of the 2 numbers is : ", j)
            break
        else:
            continue
else:
    print("HCF of the 2 numbers is : ", a)
    print("LCM of the 2 numbers is : ", a)