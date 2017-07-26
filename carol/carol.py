import bfs

def children(state):
    kids = []
    for i in range(len(state)):
        kids.append(state[:i] + state[i+1:])

    return kids

with open('dict.txt', 'r') as f:
    wordsFromFile = list(map(str.strip ,f.readlines()))

words = {}
for w in wordsFromFile:
    #truncation
    if len(w) > 9:
        continue
    sortedW = ''.join(sorted(w))
    if sortedW in words:
        words[sortedW].append(w)
    else:
        words[sortedW] = [w]

letters = input("Please enter a the letters:")
reversedLetters = ''.join(sorted(letters))

kids = children(reversedLetters)
print(kids)
print(len(kids))
