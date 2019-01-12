import itertools
import collections

class Node:
    def __init__(self, value):
        self.value = value
        self.children = collections.defaultdict(list)


def allResultsFrom(a,b):
    yield '+', a + b
    yield 'x', a * b

    c = b-a
    if c > 0:
        yield '-', c
    if b % a == 0:
        yield '/', b / a

def pairsAndRejects(numbers):
    for pair in itertools.combinations(numbers, 2):

        pair = tuple(sorted(pair))

        # We don't want to modify the original list
        rejects = list(numbers[:])
        del rejects[rejects.index(pair[0])]
        del rejects[rejects.index(pair[1])]

        yield pair, rejects

def generateTree(numbers, target, t=None):
    if t==None: t=Node(tuple(sorted(numbers)))
    # base case
    if target in numbers:
        return (t, True)
    if len(numbers) == 1: return (t, False)

    for pair, rejects in pairsAndRejects(numbers):
        a, b = pair[0], pair[1]
        for op, c in allResultsFrom(a,b):
            newNumbers = tuple(sorted(rejects + [c]))
            newNode = Node(newNumbers)
            if op in ['+', '*']:
                t.children[newNode].append(str(a) + op + str(b))
            else:
                t.children[newNode].append(str(b) + op + str(a))

        for child in t.children.keys():
            _, finished = generateTree(child.value, target, child)
            if finished: return (t, True)

    return (t, False)

def findPath(target, root):
    visited = set()
    stack = [(root, [])]

    while stack:
        (node, path) = stack.pop()

        if node not in visited:
            if target in node.value:
                return path
            visited.add(node)

            for child, operations in node.children.items():
                stack.append((child, path + [operations[0]]))


def prettyPrint(root):
    print (root.value)
    for child in root.children.keys():
        print ('\t', prettyPrint(child))

# nums = [5, 100, 25]
# t = 125

# nums = [25, 5, 3, 2]
# t = 750

# nums = [25, 75, 50, 1, 9, 3]
# t = 386

nums = [25, 75, 3, 7, 4, 2]
t = 644

# nums = [3, 6, 25, 50, 75, 100]
# t = 952

g, _ = generateTree(nums, t)
print (findPath(t, g))
