
#? Q.3: Write a function named (armstrong finder) that returns a list of Armstrong
#? numbers from 1 to upper limit (e.g., upper limit = 9999).
#? Hint: A number is said to be an Armstrong (or plus perfect) number as long as it is
#? equal to the sum of its own digits each raised to the power of the number of digits. (e.g.,
#? 153 is an Armstrong number as 153 = 1^3 + 5^3 + 3^3).
#? 

def armstrong_finder(n):
    arm=[]
    
    for i in range(1,n):
        if i>99 and i<1000:
            cube_sum = 0
            basamak = len(str(i))
            for j in str(i):
                j = int(j)
                cube_sum += j**3
            if cube_sum == i:
                arm.append(i)
        elif i>999 and i<10000:
            four_sum = 0
            for a in str(i):
                a = int(a)
                four_sum += a**4
            if four_sum == i:
                arm.append(i)
    return arm
print(armstrong_finder(9999))
        

def is_armstrong(n):
    sum_cube = 0
    for i in str(n):
        i = int(i)
        sum_cube += i**3
    if n == sum_cube:
        return True
    else:
        return False
print(is_armstrong(1634))



# 1,2,3,4,5,6,7,8,9,153,370,371,407,1634,8208,9474def f():
