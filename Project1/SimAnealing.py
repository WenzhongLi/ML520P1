# coding : utf-8
# author : GE

import sys
import Start
import math
import random
import ASTAR_MHT

class SA:
    def __init__(self):
        self.T = 0
        self.cool = 0
        self.isOne = {}
        self.isZero = {}

    def sa_init(self, init_map, size,  T, cool):
        self.T = T
        self.cool = cool
        self.init_map = init_map
        self.size = size


        new_map = [([0]*self.size) for i in  range(self.size)]
        while T > 1:
            old_cost = self.cost_cal(self.init_map)

            for i in range(0, self.size):
                for j in range(0, self.size):
                    new_map[i][j] = self.init_map[i][j]
                    if self.init_map[i][j] == 1:
                        self.isOne[(i, j)] = 1
                    elif self.init_map[i][j] == 0:
                        self.isZero[(i, j )] = 0

            self.isZero.pop((0,0))
            self.isZero.pop((self.size - 1, self.size - 1))

            length = len(new_map)
            loc = random.choice(self.isOne.keys())
            self.extend_surround(loc, new_map)
            new_cost = self.cost_cal(new_map)

            dE = new_cost - old_cost
            # print dE

            if dE >= 0 or (dE < 0 and math.exp(dE/T) > random.random):
                self.init_map = new_map


            T = T * cool
        return init_map

    # discover the node's surrounding environment
    def extend_surround(self, q, matrix):
        self.matrix = matrix
        xs = [0, -1, 1, 0]
        ys = [-1, 0, 0, 1]

        # establish new nodes by changing the given node's coordinates in 4 directions
        for xx, yy in zip(xs, ys):
            new_x, new_y = xx + q[0], yy + q[1]

            # judge if the new node is valid, a valid node means the node is inside the bound and it isn't a block
            if not self.is_valid((new_x, new_y),self.matrix):
                continue

            if random.random > 0.35:
                self.matrix[new_x][new_y] = 1
                self.isZero.pop((new_x,new_y))
                self.isOne[(new_x,new_y)] = 1

    def is_valid(self, p, matirx):
        x = p[0]
        y = p[1]
        # judge if the new node is out of bound
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return False
            # judge if the new node is a block
        if (x == 0 and y == 0) or (x==self.size - 1 and y == self.size - 1):
            return False
        return self.matrix[x][y] != 1

    def cost_cal(self, map):
        astar = ASTAR_MHT.ASTAR()
        res = astar.find_path(map, len(map))
        #  return 1, self.path, p.distance, traversal_node_count, fridge
        if res[0] == 1:
            cur_cost = res[0] * res[3]
        else:
            cur_cost = 0
        return cur_cost

if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    # set the size and density of this matrix
    size = 10
    start = Start.Start(size, 0.2)
    # start.print_matrix()
    best = -1
    for i in range(20):
        start.paint_random()
        #start.print_matrix()
        sa = SA()
        map = sa.sa_init(start.get_matrix(),size, 100, 0.98)
        astar = ASTAR_MHT.ASTAR()
        res = astar.find_path(map, len(map))
        if res[0] != 0:
            if best < res[3]:
                best = res[3]
    print best