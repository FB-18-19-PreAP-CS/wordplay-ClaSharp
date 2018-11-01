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
                    
def has_no_e():
    words = 0
    count_no_e = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                words += 1
                if 'e' in word.lower():
                    count_no_e += 0
                else:
                    count_no_e += 1
        print(float((count_no_e / words) * 100))

if __name__ == "__main__":
    #read_file()
    #at_least()
    has_no_e()
    