#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import DFS
import sys
import Start

if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    print ('start initialize')
    size = 100
    print ('start over')
    # init DFS
    dfs = DFS.DFS()
    print "density, avg_TNE"
    for i in range(0, 450):
        # every turn density increase 0.001 from 0.0-0.45
        density = float(i)/1000
        total_node_expand = 0
        count = 0;
        start = Start.Start(size, density)
        while count < 100:
            # get 100 map with a path and calculate the average numbers of nodes expanded
            start.paint_random()
            success = dfs.dfs_route(start.get_matrix(), size)
            if success[0] == 1:
                count += 1
                total_node_expand += success[3]
        print density, float(total_node_expand)/100
    print ('end')
