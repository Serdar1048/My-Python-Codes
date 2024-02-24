
#todo prime
numbers = [23, 45, 13, 7, 31, 56, 17, 29]

def is_prime(n):
    prime = True
    for i in range(2,int(n**0.5) + 1):
        if n%i == 0:
            prime = False
    return prime

list2 = [i for i in numbers if is_prime(i)]
print(list2)

#todo [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), (2, 'a'), (2, 'b'), (2, 'c'), (2, 'd'), (3, 'a'), (3, 'b'), (3, 'c'), (3, 'd'), (4, 'a'), (4, 'b'), (4, 'c'), (4, 'd')]
numbers = [1,2,3,4]
letters = "abcd"

list_2 = [(i,j) for i in numbers for j in letters ]
print(list_2)


#todo birinci listede var ikinci listede yok
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,3,6,9,5]

list3 = [ i*i for i in list1 if not i in list2]
print(list3)

#todo [1,2,3,4,5,6,7,8,9,10,11,12]
list1 = [[1,2,3],[4,5,6,7],[8,9,10,11,12]]

list2 = [j for i in list1 for j in i]
print(list2)

#todo ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
list1 = [i for i in dir(list) if not i.startswith("__")]
print(list1)