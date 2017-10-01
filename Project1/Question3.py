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
import sys
import Start
import DFS

if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    print ('start initialize')
    size = 100
    print ('start over')
    # use dfs as the fastest way to find out if there is a path
    dfs = DFS.DFS()
    # print "p" probability p of a cell being occupied as density
    # and the percentage for the maps has a path
    print "density, percentage"
    for i in range(0, 1000):
        # every turn density increase 0.001
        density = float(i)/1000
        count = 0;
        start = Start.Start(size, density)
        for t in range(0, 100):
            start.paint_random()
            success = dfs.dfs_route(start.get_matrix(), size)[0]
            # count the times of successful find a path
            if success == 1:
                count += 1
        # print "percentage: ",
        print density,
        print float(count)/100
    # dfs.dfs_route(m, size)
    print ('end')
