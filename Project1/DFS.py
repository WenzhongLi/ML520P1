#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import copy
import sys
import Start
import time


class DFS(object):
    # init this class
    def __init__(self):
        self.node_to_go = {}
        self.node_has_been = dict()
        self.size = -1
        self.min_distance = -1
        self.optimal_road = []

    # run DFS
    def dfs_route(self, map, size):
        # nodes stack
        self.node_to_go = {}
        # nodes has been to before
        self.node_has_been = dict()
        # mark this node in the stack
        node_stack_map = dict()
        # init the map and size
        for i in range(0, size):
            for j in range(0, size):
                self.node_has_been[(i, j)] = 0
                node_stack_map[(i, j)] = 0
        self.size = size
        self.min_distance = size * size
        # set start and end node
        start_node = (0, 0)
        end_node = (size - 1, size - 1)
        node_stack = [start_node]
        # init the route trace back
        tracert = dict()
        tracert[(0, 0)] = [None]
        distance = dict()
        distance[(0, 0)] = 0
        count = 0
        max_stack = 0
        while len(node_stack) > 0:
            # Get last node
            count += 1
            current_node = node_stack[len(node_stack) - 1]
            del node_stack[len(node_stack) - 1]
            node_stack_map[current_node] = 0
            current_distance = distance[current_node]
            if max_stack < len(node_stack) + 1:
                max_stack = len(node_stack) + 1
            self.node_has_been[current_node] = current_distance
            if current_distance >= self.min_distance:
                continue
            # discover this node
            # add nodes to the list end
            # -1 0
            target = (current_node[0] - 1, current_node[1])
            if self.move_to_node(target, map, current_distance + 1, size, node_stack_map):
                if target == end_node:
                    route = self.reach_end(start_node, end_node, tracert, current_distance + 1, current_node, map)
                    return 1, route, current_distance + 1, count, max_stack
                else:
                    node_stack.append(target)
                    node_stack_map[target] = 1
                    tracert[target] = current_node
                    distance[target] = current_distance + 1
            # 0 -1
            target = (current_node[0], current_node[1] - 1)
            if self.move_to_node(target, map, current_distance + 1, size, node_stack_map):
                if target == end_node:
                    route = self.reach_end(start_node, end_node, tracert, current_distance + 1, current_node, map)
                    return 1, route, current_distance + 1, count, max_stack
                else:
                    node_stack.append(target)
                    node_stack_map[target] = 1
                    tracert[target] = current_node
                    distance[target] = current_distance + 1
            # 1 0
            target = (current_node[0] + 1, current_node[1])
            if self.move_to_node(target, map, current_distance + 1, size, node_stack_map):
                if target == end_node:
                    route = self.reach_end(start_node, end_node, tracert, current_distance + 1, current_node, map)
                    return 1, route, current_distance + 1, count, max_stack
                else:
                    node_stack.append(target)
                    node_stack_map[target] = 1
                    tracert[target] = current_node
                    distance[target] = current_distance + 1
            # 0 1
            target = (current_node[0], current_node[1] + 1)
            if self.move_to_node(target, map, current_distance + 1, size, node_stack_map):
                if target == end_node:
                    route = self.reach_end(start_node, end_node, tracert, current_distance + 1, current_node, map)
                    return 1, route, current_distance + 1, count, max_stack
                else:
                    node_stack.append(target)
                    node_stack_map[target] = 1
                    tracert[target] = current_node
                    distance[target] = current_distance + 1
        return 0, None

    def move_to_node(self, target, map, distance, size, node_stack):
        if 0 <= target[0] < size \
                and 0 <= target[1] < size \
                and map[target[0]][target[1]] != 1 \
                and (self.node_has_been[target] == 0) \
                and node_stack[target] == 0:
            return 1
        else:
            return 0

    def reach_end(self, start_node, end_node, tracert, distance, current_node, map):
        # if a way has reach the end
        tracert[end_node] = current_node
        # print distance
        list = []
        list.append(end_node)
        while current_node != start_node:
            list.append(current_node)
            current_node = tracert[current_node]
        list.append(start_node)
        self.optima_road = list
        return list

    def print_optimal(self, map):
        # print the result
        print "optimal_road",
        print self.optimal_road
        print "distance:",
        print len(self.optimal_road)
        list = self.optimal_road
        result = copy.deepcopy(map)
        for node in list:
            result[node[0]][node[1]] = 2
        for k in range(self.size):
            for j in range(self.size):
                if result[k][j] == 2:
                    print "\033[1;35m2\033[0m",
                else:
                    print(result[k][j]),
            print('\n'),
        return result


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    print ('start initialize')
    # set the size and density of this matrix
    size = 10
    start = Start.Start(size, 0.3)
    # start.print_matrix()
    start.paint_random()
    # start.print_matrix()
    dfs = DFS()
    print ('start run')
    start_time = time.clock()
    # print dfs.dfs_route(start.get_matrix(), size)
    result = dfs.dfs_route(start.get_matrix(), size)
    elapsed = (time.clock() - start_time)
    print result
    print("Time used:", elapsed)
    if result[0] == 1:
        dfs.print_optimal(start.get_matrix())
        print ('over')
    else:
        print "no available way"
        print "over"