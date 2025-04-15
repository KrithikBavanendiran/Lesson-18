try:
    # num1,num2=eval(input("enter 2 numbers separated by a comma: "))
    num1=int(input("Enter a number"))
    num2=int(input("Enter a number")) 
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("Enter a number other than 0")
except SyntaxError:
    print("Enter a comma inbetween your numbers")
except:
    print("Invalid input")
else:
    print("No exceptions")
finally:
    print("This will print no matter what")