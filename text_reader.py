from math import ceil

def read_file():
    with open("words.txt") as file:
        count_the = 0
        for line in file:
            for word in line.strip().split(' '):
                #print(word)
            #print(line.strip())#strip() removes line spacing
                ##if 'the' in word.lower():
                count_the += 1
        print(count_the)
        
def at_least():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if len(word) >= 20:
                    print(word)
                    
def has_no_e(word):
    if 'e' in word.lower():
        return False
    else:
        return True
                
def no_e():
    words = 0
    count_no_e = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                words += 1
                if has_no_e(word):
                    count_no_e += 1
    p = float(count_no_e / words)
    print(f"{p * 100 :.3f}%")

def avoids(word, forbid_let):
    for letter in word:
        for ele in forbid_let:
            if forbid_let not in word.lower():
                return True
            else:
                return False
    
    
def count_avoids():
    count = 0
    forbid_let = input(str("What are the forbidden letters?\n> "))
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if avoids(word, forbid_let) == True:
                    count += 1
    print(count)
    
def uses_only(word,letters):
    '''
    >>> uses_only("aa","aa")
    True
    
    >>> uses_only("aah","ab")
    False
    '''
    for letter in word:
        for ele in letters:
            if letters in word.lower():
                return True
            else:
                return False
    
def words_with_only():
    letters = input(str("Type in letters to find a word only conatining them:\n> "))
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_only(word,letters) == True:
                    print(word)

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    #read_file()
    #at_least()
    #no_e()
    #count_avoids()
    words_with_only()