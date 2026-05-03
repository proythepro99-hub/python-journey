#Simple Calculator

num1=float(input("Enter a number: "))
operator=input("Enter an operator: ").strip()
num2=float(input("Enter a number: "))
if operator=="+":
    print(f"{num1}+{num2}={num1+num2:.3f}")
elif operator=="-":
    print(f"{num1}-{num2}={num1-num2:.3f}")
elif operator=="*":
    print(f"{num1}*{num2}={num1*num2:.3f}")
elif operator=="/":
    if num2==0:
        print("Undefined")
    else:
        print(f"{num1}/{num2}={num1/num2:.3f}")
elif operator=="//":
    if num2==0:
        print("Undefined")
    else:
        print(f"{num1}//{num2}={num1//num2}")
elif operator=="%":
    if num2==0:
        print("Undefined")
    else:
        print(f"{num1}%{num2}={num1%num2:.3f}")
elif operator=="**":
    print(f"{num1}**{num2}={num1**num2:.3f}")
else:
    print("Invalid Operator")