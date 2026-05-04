age=int(input("Enter you age: "))
if age<=0 or age>100:
    print("Invalid Age")
elif 6>age>=1:
    print("User is an infant")
elif 13>age>=6:
    print("User is a child")
elif 18>age>=13:
    print("User is a teenager")
elif 60>age>=18:
    print("User is an adult")
elif 101>age>=60:
    print("User is a senior citizen")