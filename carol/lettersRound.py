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

def solve(inputLetters):
    reversedLetters = ''.join(sorted(inputLetters))
    searcher = bfs.BFS(reversedLetters, atGoal, children)
    result = searcher.executeSearch()
    return words[result]
