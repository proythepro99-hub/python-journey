name1=input("Enter your first name: ").lower()
name2=input("Enter your last name: ").lower()
bd=input("Enter your birthdate: ").strip()
print(name1[::3]+name2[::2]+bd[::-2])