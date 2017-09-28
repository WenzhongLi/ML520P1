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
    dfs = DFS.DFS()
    print "density, avg_DT"
    for i in range(0, 450):
        density = float(i)/1000
        #print "density: ",
        #print density
        total_node_expand = 0
        count = 0;
        start = Start.Start(size, density)
        while count < 100:
            start.paint_random()
            success = dfs.dfs_route(start.get_matrix(), size)
            if success[0] == 1:
                count += 1
                total_node_expand += success[1]
        # print "percentage: ",
        print density, float(total_node_expand)/100
    # dfs.dfs_route(m, size)
    print ('end')
