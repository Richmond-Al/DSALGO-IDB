#comment
userInput=int(input("Enter the Amount of money "))
price = 100
amount = userInput / price
additional = (price%userInput)
print("Amount of Nintendo you can buy: ", amount)
print("amount of money needed for additional Wii:", additional)

userInput=int(input("Enter a number:"))
factorial=1
for x in range(1,userInput+1):
    factorial*=x
print(factorial, "is the factorial of the number 1 -", userInput)

userInput=int(input("Enter number: "))
for x in range(1, userInput+1):
    if userInput%x==0:
        print(x, "is a factor of", userInput)
