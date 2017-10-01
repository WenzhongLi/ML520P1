#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Heng-Shao Cnen
'''
import sys
import Start
import Queue
import copy
class BFS(object):
    # init the maze size and block density
    def __init__(self):
        self.node_to_go = {}
        self.node_has_been = dict()
        self.size = -1
        #self.density = density
        #self.map_matrix = []
        #for i in range(size):
        #    self.map_matrix.append([])
        #    for j in range(size):
        #        self.map_matrix[i].append(0)

    # BFS traversal
    def bfs_init(self, map, size):
        #start point
        map = copy.deepcopy(map)
        self.node_to_go = {}
        self.node_has_been = dict()
        self.size = size
        start_node = (0, 0)
        end_node = (size - 1, size - 1)
        return self.bfs(map, start_node, end_node)

    # BFS Algorithm
    def bfs(self, map, start_node, end_node):
        # Use Queue and in the first time we put the start node in Queue
        q = Queue.Queue()
        q.put(start_node)
        self.node_has_been[start_node] = (-1, -1)
        map[start_node[0]][start_node[1]] = 1
        traversal_node_count = 1
        fringe = -1

        deltaX = [0, 1, -1, 0]
        deltaY = [1, 0, 0, -1]

        distance_traveled = 0
        # Continue explore the neighbor 4 points if the neighbor point is not travel yet.
        while not q.empty():
            # each while step we add the distance by 1
            distance_traveled += 1
            currentQSize = q.qsize()
            if fringe < currentQSize:
                fringe = currentQSize
            for i in range(0, currentQSize):
                currentNode = q.get()
                for j in range(0, 4):
                    neighborNode = (currentNode[0] + deltaX[j], currentNode[1] + deltaY[j])

                    # check the boundary, if reach boundary --> continue
                    if neighborNode[0] < 0 or neighborNode[1] < 0 or neighborNode[1] \
                                    >= self.size or neighborNode[0] >= self.size:
                        continue

                    # reach the end point
                    if neighborNode == end_node:
                        self.node_has_been[neighborNode] = currentNode
                        traversal_path = []
                        target = end_node

                        # backtrack the traversal path
                        while (target != start_node):
                            traversal_path.append(target)
                            #print target
                            target = self.node_has_been.get(target)

                        # add the start_node to traversal_path
                        traversal_path.append(start_node)

                        # return (path, distance, all explore points, fringe)
                        return 1, traversal_path, distance_traveled, traversal_node_count, fringe

                    if not map[neighborNode[0]][neighborNode[1]]:
                        self.node_has_been[neighborNode] = currentNode
                        map[neighborNode[0]][neighborNode[1]] = 1
                        traversal_node_count += 1
                        q.put(neighborNode)
        #print "not distance"
        return 0, None

if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    # set the size and density of this matrix
    size = 3
    start = Start.Start(size, 0.3)
    start.print_matrix()
    start.paint_random()
    start.print_matrix()
    bfs = BFS()
    print bfs.bfs_init(start.get_matrix(), size)
    '''
    # print distance
    print "distance:"
    print distance_traveled

    print "traversal_node_count:"
    print traversal_node_count

    print "path:"
    traversal_path.reverse()
    print traversal_path

    print "fringe:"
    print fringe
    '''