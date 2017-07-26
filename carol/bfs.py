import queue

class BFS():

    def __init__(self,
                 start,
                 goalFunc,
                 childrenFunc):
        self.__currentState = start
        self.__goalFunc = goalFunc
        self.__childrenFunc = childrenFunc

        self.__q = queue.Queue(maxsize=2**19)
        self.__visted = [self.__currentState]

    def __atGoal(self):
        return self.__goalFunc(self.__currentState)

    def __children(self):
        return self.__childrenFunc(self.__currentState)

    def search(self):
        while not self.__atGoal(currentState):
            self.__visited.append(self.__currentState)
            for child in self.__children:
                if child in self.__visited:
                    continue
                else:
                    self.__q.put(child)

            self.__currentState = self.__q.get()

        return self.__currentState
