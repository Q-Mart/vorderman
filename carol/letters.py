import bfs
import db

words = db.dataBase()

def children(state):
    kids = []
    for i in range(len(state)):
        kids.append(state[:i] + state[i+1:])

    return kids

def atGoal(state):
    return state in words

reversedLetters = ''.join(sorted('ltgueourt'))

searcher = bfs.BFS(reversedLetters, atGoal, children)
print ('searching')
result = searcher.executeSearch()

print(result)
print("Length: " + str(len(result)))
print(words[result])
