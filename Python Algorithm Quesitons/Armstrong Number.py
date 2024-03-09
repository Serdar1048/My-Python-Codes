# armstrong numbers

def isArmstrong(n) :

    num1 = n % 10
    num2 = (n % 100) // 10
    num3 = n // 100
    return num1**3 + num2**3 + num3**3

isTrue = True

while isTrue:
    userNumber = int(input("Enter your number: "))
    result = isArmstrong(userNumber)
    if userNumber>=100 and userNumber<=999:
        if userNumber == result:
            print("Your Number is a Armstrong number")
            isTrue = False
        else:
            print("Your number is not a Armstrong number")
    else:
        print("düzgün sayı gir")        