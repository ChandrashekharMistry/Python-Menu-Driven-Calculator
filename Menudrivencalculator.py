def again():
    
    print("1 for Yes ")
    print("2 for No ")
    calculateAgain=int(input("Do you want to do calculate something again?? "))
    if calculateAgain==1:
        menu()
    elif calculateAgain==2:
        print("Thank for using Shekhar's calculator ")
        print("Have a Nice day")
    else:
        print("please provide valid input")
        again()
def menu():
    print(" 1 for Factorial ")
    print(" 2 for Palindrome ")
    print(" 3 for Fibionachi ")
    print(" 4 for Table of a given number")
    userInput=int(input("Enter What you want to calculate :  "))
    
    if userInput==1:
        factorial()

    elif userInput==2:
        Palindrome()
    elif userInput==3:
        Fibonachi()
    elif userInput==4:
        Table()
    else:
        print("please provide some valid input")
        menu()
    again()
def factorial():
    num=int(input("Enter no of which we have to get factorial  :    "))

    factorial = 1
    # check if the number is negative, positive or zero
    if num < 0:
     print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print("The factorial of",num,"is",factorial)

def Palindrome():
    print("Please enter word which consist of more than two letter otherwise it will not calculate Thank You")
    n=input("Enter a word and it will check whether the word is palindrome :")
    lastLetter=len(n)-1
    flag=0


    for i in range(lastLetter):

        if n[lastLetter-1]!=n[i]:
            flag=1
        
            break
    if flag==1:
    
        for j in range(lastLetter,-1,-1):
            if n[i]==n[j]:
                
                print("Yes it is a palindrome")
                break
            else :
                
                print("No it is not a palindrome")    
                break
def Fibonachi():
    n = int(input("Enter till how many number you want fibionachi series : "))
    a = 0
    b = 1
    c = 0
    while (c < n):
        print(c)
        a = b
        b = c
        c = a+b

def Table():
    
    a=1
    b=int(input("Enter the number of which you want table?"))
    for i in range(1,11):
        c=b*i   
        print(c)        

menu()