
#?Q.5: Write a function named letter frequency that i) takes a string argument (word),
#?ii) evaluates the letters and their frequencies, and iii) returns a dictionary where the
#?keys and values represent letters and their frequencies, respectively.
#?For example: Given that the word is ‘programming’ then the dictionary should contain
#?{’p’:1, ’r’:2, ’o’:1, ’g’:2, ’a’:1, ’m’:2, ’i’:1, ’n’:1}


def letter_frequency(word):
    dict={}
    for eachletter in word:
        if eachletter not in dict.keys():
            dict[eachletter]=1
        else:
            dict[eachletter]+=1
    return dict
print(letter_frequency("programming"))




def counter(word):
    word = word.lower()
    dict={}
    for i in word:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i]+=1
    return dict
print(counter("prograMming"))

