
def addition(x,y):
    return x+y

def substraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

print("Choose a mathematical operation: ")
print("1-Addition")
print("2-Substraction")
print("3-Multiplication")
print("4-Division")

selection = input("Choose a mathematical operation: ")
n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))

if selection=="1":
    print(addition(n1,n2))

elif selection=="2":
    print(substraction(n1,n2)   ) 

elif selection=="3":
    print(multiplication(n1,n2))

elif selection=="4":
    print(division(n1,n2))

else:
    print("Error")
