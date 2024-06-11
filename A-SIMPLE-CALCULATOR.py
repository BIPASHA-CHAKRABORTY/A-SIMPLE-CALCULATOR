#THIS IS MY VERY FIRST UPLOADING MY CODES- BUILDING A SIMPLE CALCULATOR 
#Hope you guys like it.


print("WELCOME TO BIPASHA`s CALCULATOR")

print("Hi,Nice to see you, Are you ready?")

num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))


print("Select a number for operation:")

print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")

sym=int(input("Select your prefered operation number:"))

if (sym==1):
    print("The addition of both the numbers are:",num1+num2)
elif(sym==2):
    print("The subtraction of both the numbers are:",num1-num2)
elif(sym==3):
    print("The division of both the numbers are:",num1/num2)
elif(sym==4):
    print("The multiplication of both the numbers are:",num1*num2)
else:
    print("SO SORRY :( Try again your operation symbol number is invalid")

#That`s my sweet little calculator as required , now let`s meet you guys at my next post till then stay tuned and connected
