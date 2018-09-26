# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == "O" or letter == "Q":
#         print(letter + "u" + suffix)
#     else:
#         print(letter + suffix)



# def find(word, letter):
#     for i in range(len(word)):
#         if word[i] == letter:
#             print(i)

# for i, letter in enumerate(team):
#     print(i, letter)


team = 'New England Patriots'
def count(s, letter):
    c = 0
    for i in s:
        if i == letter:
            c += 1
    return c

print(count(team, 'a'))