replace1=""
print("**** welcome to akku calculator**")
print("enter the first number:")
num1=int(input())
print("enter the second number:")
num2=int(input())
print("These opertions you can use:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Module")
result=0
operator=input("please choose ann option from these(1,2,3,4,5:")
if operator=="1":
    replace1="Addition"
    result=num1+num2
if operator=="2":
    if num1<num2:
        flag="Do not print"
        print("cannot subtract the first number is less than the second number")
    else:
        flag="print"
        replace1="Subtraction"
        result=num1 - num2
if operator== "3" :
    if num2==0 or num1==0:
        print("cannot multiply by zero")
    else:
        result=num1*num2
        print("The result of Multiplication of",num1,"and",num2,"is",result)
if operator=="4":
    if num2==0:
        print("cannot divided by zero")
    else:
        result=num1//num2
        print("The result of Division of",num1,"and",num2,"is",result)
if operator=="5":
    replace1="Modulus"
    result=num1%num2
    print("The result of modulus of",num1,"and",num2,"is",result)