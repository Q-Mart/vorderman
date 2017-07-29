import search
import heapq

class Astar(search.SearchAlgorithm):
    
    def __init__(self,
                 start,
                 goalFunc,
                 childrenFunc,
                 hFunc,
                 gFunc):
        search.SearchAlgorithm.__init__(self,
                                        start,
                                        goalFunc,
                                        childrenFunc)
        self.__h = hFunc
        self.__gFunc = gFunc

        self.__previous = {self._currentState: None}

        f = self.__f(self._currentState)
        self.__frontier = [(f, self._currentState)]

    def __g(self):
        return self.__gFunc(self._currentState)

    def __f(self, state):
        return self.__g() + self.__h(state)

    def __path(self):
        def Path(s):
            return ([] if (s is None) else Path(self.__previous[s]) + [s])
        s = self._currentState

    def executeSearch(self):
        while self.__frontier:
            self._currentState = heapq.heappop(self.__frontier)[1]
            self._visited.append(self._currentState)

            if self._atGoal():
               return self.__path() 

            for child in self._children():
                if child in self._visited:
                    continue

                self.__previous[child] = self._currentState
                f = self.__f(child)
                heapq.heappush(self.__frontier, (f, child))
