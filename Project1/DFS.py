#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import sys
import Start
class DFS(object):
    # 初始化迷宫大小和密度
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

    #DFS遍历
    def dfs_route(self, map, size):
        #start point
        self.node_to_go = {}
        self.node_has_been = dict()
        self.size = size
        start_node = (0, 0)
        end_node = (size - 1, size - 1)
        self.dfs_step(map, start_node, end_node, 0, [])

    def dfs_step(self, map, current_node, end_node, distance_traveled, tracert):
        if current_node[0] < 0 or current_node[1] < 0 or current_node[1] \
                >= self.size or current_node[0] >= self.size:
            return
        if map[current_node[0]][current_node[1]]:
            return
        distance_traveled+=1
        tracert.append(current_node)
        if current_node == end_node:
            print tracert
            print "success"
            return
        #print current_node
        self.node_has_been[current_node] = 1
        # +(1, 0)
        if (current_node[0]+1, current_node[1]) not in self.node_has_been:
            self.dfs_step(map, (current_node[0] + 1, current_node[1]), end_node, distance_traveled, tracert)
        # +(0, 1)
        if (current_node[0], current_node[1]+1) not in self.node_has_been:
            self.dfs_step(map, (current_node[0], current_node[1] + 1), end_node, distance_traveled, tracert)
        # +(-1, 0)
        if (current_node[0] - 1, current_node[1]) not in self.node_has_been:
            self.dfs_step(map, (current_node[0] - 1, current_node[1]), end_node, distance_traveled, tracert)
        # +(0, -1)
        if (current_node[0], current_node[1] - 1) not in self.node_has_been:
            self.dfs_step(map, (current_node[0], current_node[1] - 1), end_node, distance_traveled, tracert)
        return

if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    print ('start initialize')
    # set the size and density of this matrix
    size = 10
    start = Start.Start(size, 0.3)
    start.print_matrix()
    start.paint_random()
    start.print_matrix()
    dfs = DFS()
    dfs.dfs_route(start.get_matrix(), size)
    print ('start over')