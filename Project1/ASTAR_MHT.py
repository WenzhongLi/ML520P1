# coding : utf-8
# author : GE

import sys
import Start

# define class Node to save each node's coordinates and its parent for further use
class Node:
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

        self.open = {}
        # para close, used to store nodes that have been used
        self.close = {}
        self.path = []

    # para map, use a n*n matrix to represent the maze and the matrix is kept in this para
    def find_path(self, map, size):

        # para s_x, s_y, e_x, e_y, represent the x, y coordinates of start node and end node respectively
        self.s_x = 0
        self.s_y = 0
        self.e_x = size - 1
        self.e_y = size - 1

        self.map = map
        self.w = size
        self.h = size




        p = Node(None, self.s_x, self.s_y, 0.0)

        while True:
            open_size = self.extend_surround(p)

            if not self.open:
                # print 0, None
                return 0, None

            p = self.get_best()
            if self.is_target(p):
                self.make_path(p)
                # print "path:"
                # print self.path
                # print "distance:"
                # print p.distance
                # print "nodes_been-searched:"
                # print len(self.close)
                # print "fridge:"
                # print open_size

                return 1, self.path, p.distance, len(self.close), open_size

            self.close[(p.x, p.y)] = p
            self.open.pop((p.x, p.y))

    # make the whole path by backtracking until the node's parent is None
    def make_path(self, p):
        while p:
            self.path.append((p.x, p.y))
            p = p.parent
        self.path.reverse()

    def is_target(self, p):
        if p is not None:
            return p.x == self.e_x and p.y == self.e_y
        return False

    # choose the node, which has the highest value of F in open
    # if the value of F are the same in some node, then compare their mht distance
    def get_best(self):
        best = None
        old_value = sys.maxint
        old_mht = sys.maxint
        for i in self.open:
            value, mht = self.get_dist(i)
            if value < old_value:
                best = self.open.get(i)
                old_value = value
                old_mht = mht
            elif value == old_value and mht < old_mht:
                best = self.open.get(i)
                old_value = value
                old_mht = mht
        return best


    def get_dist(self, i):
        mht = (self.e_x - i[0]) + (self.e_y - i[1])
        return self.open.get(i).distance + mht, mht

    # discover the node's surrounding environment
    def extend_surround(self, q):
        xs = [0, -1, 1, 0]
        ys = [-1, 0, 0, 1]
        open_size = 0
        # establish new nodes by changing the given node's coordinates in 4 directions
        for xx, yy in zip(xs,ys):
            new_x,  new_y = xx + q.x, yy + q.y

            #judge if the new node is valid, a valid node means the node is inside the bound and it isn't a block
            if not self.is_valid(new_x, new_y):
                continue

            node = Node(q, new_x, new_y, q.distance + 1)
            if self.close.has_key((node.x, node.y)):
                continue

            if self.open.has_key((node.x, node.y)):
                if self.open.get((node.x, node.y)).distance > node.distance:
                    self.open[(node.x, node.y)] = node
                continue
            self.open[(node.x, node.y)] = node

        if open_size < len(self.open):
            open_size = len(self.open)
        return open_size

    def is_valid(self, x, y):
        # judge if the new node is out of bound
        if x < 0 or x >= self.w or y < 0 or y >= self.h:
            return False

        #judge if the new node is a block
        return self.map[x][y] != 1


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argument", i, sys.argv[i]
    # set the size and density of this matrix
    size = 3000
    start = Start.Start(size, 0.2)
    # start.print_matrix()
    start.paint_random()
    # start.print_matrix()
    astar = ASTAR()
    astar.find_path(start.get_matrix(), size)
