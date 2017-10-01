# coding : utf-8
#author : GE

import sys
import Start
import DFS
import BFS

if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    print ('start initialize')
    size = 100
    print ('start over')
    dfs = DFS.DFS()
    bfs = BFS.BFS()
    # print "p" probability p of a cell being occupied as density
    # print Length for the average shortest path length
    print "density, Length"
    for i in range(0, 450):
        # every turn density increase 0.001,from 0-0.45
        density = float(i)/1000
        count = 0
        success_3_count1 = 0
        success_3_count2 = 0
        start = Start.Start(size, density)
        # get 100 map with a path and calculate the average path length
        while count < 100:
            start.paint_random()
            success1 = dfs.dfs_route(start.get_matrix(), size)
            success2 = bfs.bfs_init(start.get_matrix(), size)
            # for every time find a path, get the average path length
            if success1[0] == 1:
                count += 1
                success_3_count1 += success1[2]
            if success2[0] == 1:
                count += 1
                success_3_count2 += success2[2]
        print density,
        print float(success_3_count1)/100, float(success_3_count2)/100
    print ('end')