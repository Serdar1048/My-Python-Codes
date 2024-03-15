#Coprime Number

def isCompire(x,y):
    for i in range(2,x+1):
        if x%i==0 and y%i==0:
            return False #aralarında asla değildir
    return True #aralarında asaldır
    

a = isCompire(22,33)
print(a)
if a == True:
    print("it is coprime number")
elif a == False:
    print("it is not coprime number")
