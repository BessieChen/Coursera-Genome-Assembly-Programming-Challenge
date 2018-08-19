# python3

import sys

class Eulerian_Cycle:
    def __init__( self ):
        self.number_of_explored_edges = 0
        self.position_of_unused_node = dict()
        self.path = []
        isBalanced = self._input()
        if not isBalanced:
            print('0')
        else:
            print('1')
            self.calculateEulerianCycle()
            self.printPath()

    def _input( self ):
        data = list(sys.stdin.read().strip().split())
        self.n, self.number_of_explored_edges = int(data[0]), int(data[1])
        self.unusedEdges = [[] for _ in range(self.n)]
        self.adj = [[] for _ in range(self.n)]
        self.outDeg = [0] * self.n
        self.inDeg = [0] * self.n
        self.adj_current_position = [0] * self.n
        for i in range(self.number_of_explored_edges):
            curFrom = int(data[2 * i + 2]) - 1
            curTo = int(data[2 * i + 3]) - 1
            self.adj[curFrom].append(curTo)
            self.outDeg[curFrom] += 1
            self.inDeg[curTo] += 1
        for i in range(self.n):
            if self.outDeg[i] != self.inDeg[i]:
                return False
        return True


    def updatePath(self, startPos):
        l = len(self.path) - 1
        self.path = self.path[startPos:l] + self.path[:startPos]
        for node, pos in self.position_of_unused_node.items():
            if pos < startPos:
                self.position_of_unused_node[node] = pos + l - startPos
            else:
                self.position_of_unused_node[node] = pos - startPos
        return

    def explore( self, s ):
        self.path.append(s)
        curPos = self.adj_current_position[s]
        curMaxPos = self.outDeg[s]
        while curPos < curMaxPos:
            self.adj_current_position[s] = curPos + 1
            if curPos + 1 < curMaxPos:
                self.position_of_unused_node[s] = len(self.path) - 1
            else:
                if s in self.position_of_unused_node:
                    del self.position_of_unused_node[s]
            v = self.adj[s][curPos]
            self.path.append(v)
            s = v
            curPos = self.adj_current_position[s]
            curMaxPos = self.outDeg[s]
            self.number_of_explored_edges -= 1
        return

    def calculateEulerianCycle( self ):
        self.explore(1)
        while self.number_of_explored_edges > 0:
            node, pos = self.position_of_unused_node.popitem()
            self.updatePath(pos)
            self.explore(node)
        return self.path

    def printPath( self ):
        print(' '.join([str(node + 1) for node in self.path[:-1]]))


if __name__ == "__main__":
    Eulerian_Cycle()