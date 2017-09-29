#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import copy
import json
import sys
sys.path.append("..")
import Start
import BFS
import DFS

if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    print ('start initialize')

    size = 10
    start = Start.Start(size, 0.3)
    start.paint_random()
    start.print_matrix()
    map = copy.copy(start.get_matrix())
    data = dict()
    original = {"size": size, "map": map}#[[1,1,1],[1,1,1],[1,1,1]]}
    data["original"] = original
    json = json.dumps(data)
    print json


    size = 100
    # start.print_matrix()
    # start.paint_random()
    # start.print_matrix()
    print ('start over')
    bfs = BFS.BFS()
    # dfs.dfs_route(start.get_matrix(), size)
    print "density, percentage"
    for i in range(0, 450):
        density = float(i)/1000
        # print "density: ",
        # print density

        count = 0;
        success_3_count = 0;
        start = Start.Start(size, density)
        while count < 100:
            start.paint_random()
            success = bfs.bfs_init(start.get_matrix(), size)
            if success[0] == 1:
                count += 1
                success_3_count += success[2]
        # print "percentage: ",
        print density,
        print float(success_3_count)/100
    # dfs.dfs_route(m, size)
    print ('end')