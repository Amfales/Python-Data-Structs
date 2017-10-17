class UnweightedGraph():
    def __init__(self):
        self._n = {}


    def findAllPaths(self,startNode,endNode,path=[]):
        path = path + [startNode]
        if startNode == endNode:
            return [path]
        if startNode not in self._n.keys():
            return []
        paths = []
        for nextNode in self._n[startNode]:
            if nextNode not in path:
                newpaths = self.findAllPaths(nextNode,endNode,path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def findShortestPath(self,startNode,endNode,path=[]):
        path = path + [startNode]
        if startNode == endNode:
            return path
        if startNode not in self._n.keys():
            return None
        shortest = None
        for nextNode in self._n[startNode]:
            if nextNode not in path:
                newpath = self.findShortestPath(nextNode,endNode,path)
                if newpath:
                    if shortest is None or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def addEdge(self,fromVertex,toVertex):
        if fromVertex not in self._n:
            self.addNode(fromVertex)
        if toVertex not in self._n:
            self.addNode(toVertex)
        self._n[fromVertex].append(toVertex)
        

    def addNode(self,node):
        self._n[node] = list()


class Vertex():
    def __init__(self,ident=None):
        self._i = ident

    def getID(self):
        return self._i



_from = 0
_to = 0
def main():
    global _from,_to
    print("Initializing Graph...")
    g = UnweightedGraph()
    _from = "AABBCDEF"
    _to   = "BCCDDCFC"
    print('\n'.join('->'.join([x[0],x[1]]) for x in zip(_from,_to)))
    for together in zip(_from,_to):
        g.addEdge(together[0],together[1])
    print("Finding all paths from A -> D")
    print(g.findAllPaths("A","D"))
    print("Finding shortest path from A -> D")
    print(g.findShortestPath("A","D"))


if __name__ == '__main__':
    main()
