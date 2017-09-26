#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import copy
import sys
import Start


class DFS(object):
    # 初始化迷宫大小和密度
    def __init__(self):
        self.node_to_go = {}
        self.node_has_been = dict()
        self.size = -1
        self.min_distance = -1
        self.optimal_road = []

    # DFS遍历
    def dfs_route(self, map, size):
        # start point
        self.node_to_go = {}
        self.node_has_been = dict()
        node_stack_map = dict()
        # self.node_has_been[(0, 0)] = 0
        for i in range(0, size):
            for j in range(0, size):
                self.node_has_been[(i, j)] = 0
                node_stack_map[(i, j)] = 0
        self.size = size
        self.min_distance = size * size
        start_node = (0, 0)
        end_node = (size - 1, size - 1)
        node_stack = [start_node]
        tracert = dict()
        tracert[(0, 0)] = [None]
        distance = dict()
        distance[(0, 0)] = 0
        while len(node_stack) > 0:
            # Get last node
            current_node = node_stack[len(node_stack) - 1]
            del node_stack[len(node_stack) - 1]
            node_stack_map[current_node] = 0
            current_distance = distance[current_node]
            self.node_has_been[current_node] = current_distance
            if current_distance >= self.min_distance:
                continue
            # discover this node
            # add nodes to the list end
            # -1 0
            target = (current_node[0] - 1, current_node[1])
            if self.move_to_node(target, map, current_distance + 1, size, node_stack_map):
                if target == end_node:
                    self.reach_end(start_node, end_node, tracert, current_distance + 1, current_node)
                else:
                    node_stack.append(target)
                    node_stack_map[target] = 1
                    tracert[target] = current_node
                    distance[target] = current_distance + 1
            # 0 -1
            target = (current_node[0], current_node[1] - 1)
            if self.move_to_node(target, map, current_distance + 1, size, node_stack_map):
                if target == end_node:
                    self.reach_end(start_node, end_node, tracert, current_distance + 1, current_node)
                else:
                    node_stack.append(target)
                    node_stack_map[target] = 1
                    tracert[target] = current_node
                    distance[target] = current_distance + 1
            # 1 0
            target = (current_node[0] + 1, current_node[1])
            if self.move_to_node(target, map, current_distance + 1, size, node_stack_map):
                if target == end_node:
                    self.reach_end(start_node, end_node, tracert, current_distance + 1, current_node)
                else:
                    node_stack.append(target)
                    node_stack_map[target] = 1
                    tracert[target] = current_node
                    distance[target] = current_distance + 1
            # 0 1
            target = (current_node[0], current_node[1] + 1)
            if self.move_to_node(target, map, current_distance + 1, size, node_stack_map):
                if target == end_node:
                    self.reach_end(start_node, end_node, tracert, current_distance + 1, current_node)
                else:
                    node_stack.append(target)
                    node_stack_map[target] = 1
                    tracert[target] = current_node
                    distance[target] = current_distance + 1

        if self.min_distance < size * size:
            list = []
            current_node = end_node
            while current_node != start_node:
                list.append(current_node)
                current_node = tracert[current_node]
            list.append(start_node)
            self.optimal_road = list
            print "optimal_road",
            print self.optimal_road
            print "distance:",
            print len(self.optimal_road)
            result = copy.deepcopy(map)
            for node in self.optimal_road:
                result[node[0]][node[1]] = 2
            for k in range(size):
                for j in range(size):
                    if result[k][j] == 2:
                        print "\033[1;35m2\033[0m",
                    else:
                        print(result[k][j]),
                print('\n'),

    def move_to_node(self, target, map, distance, size, node_stack):
        if 0 <= target[0] < size \
                and 0 <= target[1] < size \
                and map[target[0]][target[1]] != 1 \
                and (self.node_has_been[target] == 0 or self.node_has_been[target] > distance) \
                and node_stack[target] == 0:
            return 1
        else:
            return 0

    def reach_end(self, start_node, end_node, tracert, distance, current_node):
        if distance < self.min_distance:
            tracert[end_node] = current_node
            print distance
            # list = []
            # list.append(end_node)
            # while current_node != start_node:
            #     list.append(current_node)
            #     current_node = tracert[current_node]
            # list.append(start_node)
#
            # # print list
            # # print end_nod
            # # if len(list) < self.min_distance:
            self.min_distance = distance  # len(list)
            # self.optimal_road = list
        return


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    print ('start initialize')
    # set the size and density of this matrix
    size = 300
    start = Start.Start(size, 0.3)
    start.print_matrix()
    start.paint_random()
    start.print_matrix()
    print ('start over')
    dfs = DFS()
    m = [[0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 1],
         [0, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 1, 0],
         [0, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0]]
    dfs.dfs_route(start.get_matrix(), size)
    # dfs.dfs_route(m, size)
    print ('end')
