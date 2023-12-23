num = int(input("Enter your desired number : "))#Asking the user for a number that they want the table of
i = 1#inititializing the multiplicator 
while i <= 10:#using while loop to run until multiplicator shows 10
    print(f"{num} x {i} = ", num*i)#Printing it out to show the table
    i+=1#Incrementing it so that the table does not get stuck on x '1' only
    