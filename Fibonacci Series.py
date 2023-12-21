num = int(input("Enter your desired number : "))
a=0
b=1
print(a,b, end='')
for i in range(0,num-2):
    c=a+b
    a=b
    b=c
    print(b, end='')
print(f"Your {num} term is : ", b)