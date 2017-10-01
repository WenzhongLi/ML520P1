#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import sys
import Start
import BFS

if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    print ('start initialize')
    size = 100
    print ('start over')
    bfs = BFS.BFS()
    # print "p" probability p of a cell being occupied as density
    # print Length for the average shortest path length
    print "density, Length"
    for i in range(0, 450):
        # every turn density increase 0.001,from 0-0.45
        density = float(i)/1000
        count = 0;
        success_3_count = 0;
        start = Start.Start(size, density)
        # get 100 map with a path and calculate the average path length
        while count < 100:
            start.paint_random()
            success = bfs.bfs_init(start.get_matrix(), size)
            # for every time find a path, get the average path length
            if success[0] == 1:
                count += 1
                success_3_count += success[2]
        print density,
        print float(success_3_count)/100
    print ('end')