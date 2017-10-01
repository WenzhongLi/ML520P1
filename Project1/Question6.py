#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import DFS
import ASTAR_MHT
import ASTAR_EUC
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
    a_mht = ASTAR_MHT.ASTAR()
    a_euc = ASTAR_EUC.ASTAR()
    # print "p" probability p of a cell being occupied as density
    # and the total nodes expanded for both A*
    print "density, avg_TNE_mht, avg_TNE_euc"
    # p from 0-0.45 increase 0.005 every turn
    for i in range(0, 90):
        density = float(i)/200
        total_node_expand_r1 = 0
        total_node_expand_r2 = 0
        count = 0;
        start = Start.Start(size, density)
        # get 100 map with a path and calculate the average numbers of nodes expanded
        while count < 100:
            start.paint_random()
            success = dfs.dfs_route(start.get_matrix(), size)
            if success[0] == 1:
                count += 1
                r1 = a_mht.find_path(start.get_matrix(), size)[3]
                r2 = a_euc.find_path(start.get_matrix(), size)[3]
                total_node_expand_r1 += r1
                total_node_expand_r2 += r2
        print density, float(total_node_expand_r1)/100, float(total_node_expand_r2)/100
    print ('end')
