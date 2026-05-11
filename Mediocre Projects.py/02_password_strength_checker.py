password=input("Enter your password: ")
up=False
low=False
num=False
for ch in password:
    if ch.isupper():
        up=True
    if ch.islower():
        low=True
    if ch.isdigit():
        num=True
if len(password)>8 and up and low and num:
    print(f"\"{password}\" is a strong password, it meets all the criterias")
else:
    print(f"\"{password}\" is a weak passsword, it doesn't meet all the criterias")