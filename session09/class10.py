fin = open("session09/words.txt")
line = fin.readline()

def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for i in required:
        if i not in word:
            return False
    return True


print(uses_all('Babson', 'abs'))
print(uses_all('college', 'abs'))

def uses_all_fin(required):
    cnt = 0
    for i in fin:
        i = i.strip()
        if uses_all(i,required):
            print(i)
            cnt = cnt + 1
    print(cnt)

uses_all_fin('aeiou')

def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

fin = open("session09/words.txt")

def finds_all_abc():
    cnt = 0
    for i in fin:
        i = i.strip()
        if is_abecedarian(i):
            print(i)
            cnt = cnt + 1
    print(cnt)

# finds_all_abc()

def find_longest():
    dummy = ''
    for i in fin:
        word = i.strip()
        if is_abecedarian(word):
            if len(word) > len(dummy):
                print(word)
                dummy = word

find_longest()


    # counter = 0
    # previous = word[0]
    # while counter <= len(word):
    #     counter = counter + 1
    #     if word[counter] < previous:
    #         previous = word[counter]
    #         return False
        


