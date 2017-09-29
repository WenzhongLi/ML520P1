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
    print "density, avg_TNE_mht, avg_TNE_euc"
    for i in range(0, 90):
        density = float(i)/200
        #print "density: ",
        #print density
        total_node_expand_r1 = 0
        total_node_expand_r2 = 0
        count = 0;
        start = Start.Start(size, density)
        while count < 100:
            start.paint_random()
            success = dfs.dfs_route(start.get_matrix(), size)
            if success[0] == 1:
                count += 1
                r1 = a_mht.find_path(start.get_matrix(), size)[4]
                r2 = a_euc.find_path(start.get_matrix(), size)[4]
                total_node_expand_r1 += r1
                total_node_expand_r2 += r2
        # print "percentage: ",
        print density, float(total_node_expand_r1)/100, float(total_node_expand_r2)/100
    # dfs.dfs_route(m, size)
    print ('end')
