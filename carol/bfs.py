import search
import queue

class BFS(search.SearchAlgorithm):

    def __init__(self,
                 start,
                 goalFunc,
                 childrenFunc):
        search.SearchAlgorithm.__init__(self,
                                        start,
                                        goalFunc,
                                        childrenFunc)
        self.__q = queue.Queue(maxsize=2**19)

    def executeSearch(self):
        while not self._atGoal():
            self._visited.append(self._currentState)
            for child in self._children():
                if child in self._visited:
                    continue
                else:
                    self.__q.put(child)

            self._currentState = self.__q.get()

        return self._currentState
