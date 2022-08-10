print("----------welcome th the zodiac calculator")
print("Enter the number1 :")
num1=int(input())
print("Enter the number2 :")
num2=int(input())
print("These are the opertion you can use :")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.modulus")
a=input("Please choose an option from these (1,2,3,4,5):")
if a=="1":
    print("Addition")
    print("sum of the number is:",num1+num2)
if a=="2":
    print("Subtraction")
    print("The difference of the two number is :",num1 - num2)
if a=="3":
    print("Multiplication")
    print("The product of the two number is :",num1 * num2)
if a=="4":
    print("Division")
    print("The division of the two number is :",num1 / num2)
if a=="5":
    print("Module")
    print("The module of the two number is :",num1 % num2)


