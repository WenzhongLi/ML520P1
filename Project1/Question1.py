#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import time
import DFS
import BFS
import ASTAR_MHT
import ASTAR_EUC
import sys
import Start

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
    # init all the algorithm
    dfs = DFS.DFS()
    bfs = BFS.BFS()
    a_mht = ASTAR_MHT.ASTAR()
    a_euc = ASTAR_EUC.ASTAR()
    print ('start run')
    print "DIM, T_DFS, T_BFS, T_MHT, T_EUC"
    while 1:
        print size,
        start = Start.Start(size, 0.3)
        start.paint_random()
        while dfs.dfs_route(start.get_matrix(), size)[0] == 0:
            start.paint_random()
        # set timer for each algorithm
        start_time = time.clock()
        #DFS
        dfs.dfs_route(start.get_matrix(), size)
        T_DFS = (time.clock() - start_time)

        start_time = time.clock()
        #BFS
        bfs.bfs_init(start.get_matrix(), size)
        T_BFS = (time.clock() - start_time)

        start_time = time.clock()
        #A_MHT
        a_mht.find_path(start.get_matrix(), size)
        T_MHT = (time.clock() - start_time)

        start_time = time.clock()
        #A_EUC
        a_euc.find_path(start.get_matrix(), size)
        T_EUC = (time.clock() - start_time)
        print T_DFS, T_BFS, T_MHT, T_EUC
        # print the result and if one algorithm exceed 60s end the test
        if T_DFS > 60 or T_BFS > 60 or T_MHT > 60 or T_EUC > 60:
            break
        # every turn size = size * 110%
        size = int(size * 1.1)
    print "end"