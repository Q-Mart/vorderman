import astar
import collections
import operator

State = collections.namedtuple('State', ['currentVal', 'numbersLeft', 'lastOperation'])

def solveNumbersRound(goal, numbers):

    goalFunc = lambda x: x.currentVal == goal
    hFunc = lambda x: goal - x.currentVal
    gFunc = hFunc

    def children(s):
        operators = [('+', operator.add),
                     ('-', operator.sub),
                     ('*', operator.mul),
                     ('/', operator.truediv)]
        kids = []
        for n in s.numbersLeft:
            for ch, op in operators:
                i = s.numbersLeft.index(n)
                newNumbersLeft = s.numbersLeft[i+1:] + s.numbersLeft[:i]
                newCurrentVal = op(s.currentVal, n)

                kids.append(State(newCurrentVal, newNumbersLeft, ch))

        return kids

    searcher = astar.Astar(State(0, numbers, None), goalFunc, children, hFunc, gFunc)
    return searcher.executeSearch()

r = solveNumbersRound(386.0, (25, 75, 50, 1, 9, 3))
print(r)
