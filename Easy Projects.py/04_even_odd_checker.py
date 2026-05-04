number=int(input("Enter a number: "))
if number==0:
    print(f"{number} is neither odd nor even")
elif number%2==0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")