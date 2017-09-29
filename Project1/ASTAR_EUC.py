# coding : utf-8
# author : GE

import sys
import Start
import math

class Node :
    def __init__(self, parent, x, y, distance):
        self.parent = parent
        self.x = x
        self.y = y
        self.distance = distance

class ASTAR:
        def __init__(self):
            self.s_x = 0
            self.s_y = 0
            self.e_x = 0
            self.e_y = 0

            self.map = None
            self.w = 0
            self.h = 0

            self.open = []
            self.close = []
            self.path = []

        def find_path(self, map, size):
            self.s_x = 0
            self.s_y = 0
            self.e_x = size - 1
            self.e_y = size - 1

            self.map = map
            self.w = len(map)
            self.h = len(map)

            self.open = []
            self.close = []
            self.path = []

            p = Node(None, self.s_x, self.s_y, 0.0)
            traversal_node_count = 0

            while True:
                traversal_node_count += 1
                openSize = self.extend_round(p)



                if not self.open:
                    return

                idx, p = self.get_best()

                if self.is_target(p):
                    self.make_path(p)
                    print "path:"
                    print self.path
                    print "distance:"
                    print p.distance
                    print "node_been_searched:"
                    print traversal_node_count
                    print "fridge:"
                    print openSize
                    # return 1, path, total_distance, node_has_searched, fridge
                    return 1, self.path, p.distance, traversal_node_count, openSize

                self.close.append(p)
                del self.open[idx]


        def make_path(self, p):
            while p:
                self.path.append((p.x, p.y))
                p = p.parent
            self.path.reverse()

        def is_target(self, p):
            if p != None:
                return p.x == self.e_x and p.y == self.e_y
            return False

        def get_best(self):
            best = None
            old_value = sys.maxint
            old_euc = sys.maxint
            best_idx = -1
            for idx, i in enumerate(self.open):
                value, euc = self.get_dist(i)
                if value < old_value:
                    best = i
                    best_idx = idx
                    old_value = value
                    old_euc = euc
                elif value == old_value and euc < old_euc:
                    best = i
                    best_idx = idx
                    old_value = value
                    old_euc = euc


            return best_idx, best


        def get_dist(self, i):
            euc = math.sqrt((self.e_x - i.x) * (self.e_x - i.x) + (self.e_y - i.y) * (self.e_y - i.y))
            return i.distance + euc, euc


        def extend_round(self, q):
            xs = [0, -1, 1, 0]
            ys = [-1, 0, 0, 1]
            openMax = 0

            for xx, yy in zip(xs,ys):
                new_x, new_y = xx + q.x , yy + q.y

                if not self.is_valid_coord(new_x, new_y):
                    continue

                node = Node(q, new_x, new_y,  q.distance + 1)
                if self.node_in_close(node):
                    continue

                i = self.node_in_open(node)
                if i != -1:
                    if self.open[i].distance > node.distance:
                        self.open[i].parent = q
                        self.open[i].distance = node.distance
                    continue
                self.open.append(node)

            if openMax < len(self.open):
                openMax = len(self.open)
            return openMax

        def node_in_close(self, node):
            for i in self.close:
                if node.x == i.x and node.y == i.y:
                    return True
            return False

        def node_in_open(self, node):

            for i, n in enumerate(self.open):
                if node.x == n.x and node.y == n.y:
                    return i
            return -1

        def is_valid_coord(self, x, y):
            if x < 0 or x >= self.w or y < 0 or y >= self.h:
                return False
            return self.map[x][y] != 1


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    # set the size and density of this matrix
    size = 100
    start = Start.Start(size, 0.3)
    start.print_matrix()
    start.paint_random()
    start.print_matrix()
    astar = ASTAR()
    astar.find_path(start.get_matrix(), size)
