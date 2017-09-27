# coding : utf-8
#author : GE

import sys
import Start
import Queue


class ComparableObj(object):
    def __init__(self, distance_traveled, ManhattanDis, node):
        self.distance_traveled = distance_traveled
        self.ManhattanDis = ManhattanDis
        self.node = node

    def __cmp__(self, other):
        return cmp(self.distance_traveled + self.ManhattanDis, other.distance_traveled + other.ManhattanDis)


class ASTAR(object):
    def __init__(self):
        self.node_to_go = {}
        self.node_has_been = dict()
        self.size = -1
        self.node_to_poo = {}

    # ASTAR
    def astar_init(self, map, size):
        # start point
        self.node_to_go = {}
        self.node_has_been = dict()
        self.size = size
        start_node = (0, 0)
        end_node = (size - 1, size - 1)
        self.astar(map, start_node, end_node)

    def astar(self, map, start_node, end_node):
        q = Queue.PriorityQueue()
        q.put(ComparableObj(0, end_node[0] + end_node[1] - start_node[0] - start_node[1], start_node))
        self.node_has_been[start_node] = (-1, -1)
        map[start_node[0]][start_node[1]] = 1
        deltaX = [0, 1, -1, 0]
        deltaY = [1, 0, 0, -1]
    
        distance_traveled = 0
        optimial_distance = 0
        while not q.empty():
            distance_traveled += 1
            currentQSize = q.qsize()
            for i in range(0, currentQSize):
                currentObj = q.get()
                currentNode = currentObj.node
                for j in range(0, 4):
                    neighborNode = (currentNode[0] + deltaX[j], currentNode[1] + deltaY[j])

                    if neighborNode[0] < 0 or neighborNode[1] < 0 or neighborNode[1] \
                            >= self.size or neighborNode[0] >= self.size:
                        continue

                    if neighborNode == end_node:
                        self.node_has_been[neighborNode] = currentNode
                        target = end_node


                        while (target != start_node):
                            print target
                            optimial_distance = optimial_distance + 1
                            for (k, v) in self.node_has_been.items():
                                if k == target:
                                    buf = self.node_has_been.get(k)
                                    target = buf
                                    break
                        print start_node

                        # print distance
                        print "distance:"
                        print optimial_distance
                        return
                    if not map[neighborNode[0]][neighborNode[1]]:
                        self.node_has_been[neighborNode] = currentNode
                        map[neighborNode[0]][neighborNode[1]] = 1
                        q.put(ComparableObj(distance_traveled,
                                            end_node[0] + end_node[1] - neighborNode[0] - neighborNode[1],
                                            neighborNode))
        print "not distance"


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    # set the size and density of this matrix
    size = 200
    start = Start.Start(size, 0.2)
    start.print_matrix()
    start.paint_random()
    start.print_matrix()
    astar = ASTAR()
    astar.astar_init(start.get_matrix(), size)