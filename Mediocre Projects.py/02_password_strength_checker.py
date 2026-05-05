password=input("Enter password: ")
up=any(i.isupper()for i in password)
low=any(i.islower()for i in password)
num=any(i.isdigit()for i in password)
if len(password)>8 and up and low and num:
    print("Password is strong")
else:
    print("Password is weak")