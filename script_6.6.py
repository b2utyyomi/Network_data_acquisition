print()
name=input("Please enter your first name: ")
age=input("Please enter your age: ")
print()
if(age.isdigit()):
	print(name, ":", sep="")
	print("In ten years your age will be:", int(age)+10)
else:
	print("Sorry", name, "the age you entered is not a number")
print()
