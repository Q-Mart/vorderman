import bfs

def children(state):
    kids = []
    for i in range(len(state)):
        kids.append(state[:i] + state[i+1:])

    return kids

def atGoal(state):
    return state in words

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

letters = input("Please enter all the letters: ")
reversedLetters = ''.join(sorted(letters))

searcher = bfs.BFS(reversedLetters, atGoal, children)
result = searcher.executeSearch()

print(result)
print("Length: " + str(len(result)))
print(words[result])
