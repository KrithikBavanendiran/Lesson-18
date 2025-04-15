try:
    age=int(input("enter your age: "))
    print(age)

    even=age%2
    if even==0:
        print("Your age is even")
    else:
        print("Your age is odd")

except ValueError:
    print("Did you enter something other than a number?")