import itertools
import collections

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

def generateTree(numbers, target):
    numbers = tuple(sorted(numbers))
    graph = collections.defaultdict(list)

    # node represented in dict as ('operation to get here', list of numbers)
    def r(node):
        numbers = node[1]
        for pair, rejects in pairsAndRejects(numbers):
            a,b = pair[0], pair[1]
            for op, c in allResultsFrom(a, b):
                newNumbers = tuple(sorted(rejects + [c]))
                if op in ['+', '*']:
                    newNode = ((str(a) + op + str(b), newNumbers))
                else:
                    newNode = ((str(b) + op + str(a), newNumbers))

                graph[node].append(newNode)
                r(newNode)

    r(('', numbers))
    return graph


def findPath(target, start, graph):
    start = ('', tuple(sorted(start)))

    visited = set()
    stack = [(start, [start])]

    while stack:
        (node, path) = stack.pop()

        if node[1] not in visited:
            if target in node[1]:
                return path
            visited.add(node[1])

            for c in graph[node]:
                stack.append((c, path + [c]))


def prettyPrint(root):
    print (root.value)
    for child in root.children.keys():
        print ('\t', prettyPrint(child))

def printPath(path):
    for op, nums in path:
        print (op, '\t', nums)

def solve(target, numbers):
    g = generateTree(numbers, target)
    return findPath(target, numbers, g)

def test(target, numbers):
    printPath(solve(target, numbers))

# Testing
if __name__ == '__main__':
    print ('Solving Case 1...')
    test(125, [5, 100,25])

    print ('Solving Case 2...')
    test(750, [25, 5, 3, 2])

    print ('Solving Case 3...')
    test(386, [25, 75, 50, 1, 9, 3])

    print ('Solving Case 4...')
    test(644, [25, 75, 3, 7, 4, 2])

    print ('Solving Case 5...')
    test(952, [3, 6, 25, 50, 75, 100])
