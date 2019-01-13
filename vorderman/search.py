class SearchAlgorithm():
    
    def __init__(self,
                 start,
                 goalFunc,
                 childrenFunc):
        self._currentState = start
        self._goalFunc = goalFunc
        self._childrenFunc = childrenFunc
        self._visited = [self._currentState]

    def _atGoal(self):
        return self._goalFunc(self._currentState)

    def _children(self):
        return self._childrenFunc(self._currentState)

    def executeSearch(self):
        raise NotImplementedError
