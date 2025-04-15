try:
    number=int(input("enter your age: "))
    print("Your age is",number)
except ValueError as v:
    print(v)

