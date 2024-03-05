
#? Q.7: Write a function named merge that i) takes two lists (L1, L2) where the numbers
#? are stored in ascending order, ii) merges them into a list such that the numbers after
#? the merge are also stored in ascending order, and finally iii) returns the list.
#? Note that, as shown in the comments below, the lengths of the input lists can be
#? different and vary.
#? Note also that you do not use any of the built-in sorting functions or methods from
#? Python.

def merge(L1, L2):
# L1 and L2 are lists of integers,
# Merges L1 and L2 in ascending order into a list,
# Returns that list.
# e.g.:
# L1 = [3, 7, 9, 11]
# L2 = [1, 5, 7, 12, 13, 19]
# list to be returned = [1, 3, 5, 7, 7, 9, 11, 12, 13, 19]

    bos = []
    i, j = 0, 0

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            bos.append(L1[i])
            i += 1
        else:
            bos.append(L2[j])
            j += 1

 
    # Kalan elemanları ekleyin
    while i < len(L1):
        bos.append(L1[i])
        i += 1

    while j < len(L2):
        bos.append(L2[j])
        j += 1
        
    return bos
print(merge([3, 7, 9, 11],[1, 5, 7, 12, 13, 19]))












def merge(l1,l2):
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    else:
        if l1[0] > l2[0]:
            return [l2[0]] + merge(l1,l2[1:])
        else:
            return [l1[0]] + merge(l1[1:],l2)



print(merge([3, 7, 9, 11],[1, 5, 7, 12, 13, 19]))
