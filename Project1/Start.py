#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''

import random
import sys


class Start(object):
    # init size and density of maze
    def __init__(self, size, density):
        self.size = size
        self.density = density
        self.map_matrix = []
        for i in range(size):
            self.map_matrix.append([])
            for j in range(size):
                self.map_matrix[i].append(0)

    # print maze to commend line
    def print_matrix(self):
        count_blocked = 0
        for i in range(self.size):
            for j in range(self.size):
                print(self.map_matrix[i][j]),
                if self.map_matrix[i][j]:
                    count_blocked+=1
            print('\n'),
        print(str(count_blocked)+" are blocked\n")

    # paint maze randomly
    def paint_random(self):
        matrix = [[0 for j in range(self.size)] for k in range(self.size)]
        list = []
        # init a set of all point could be block
        for i in range(self.size):
            for j in range(self.size):
                list.append((i, j))
        del list[self.size * self.size - 1]
        del list[0]
        dot_num = int(self.size * self.size * self.density)
        if dot_num > self.size * self.size - 2:
            dot_num = self.size * self.size - 2
        # get some point randomly
        slice = random.sample(list, dot_num)
        # Paint them 1
        for node in slice:
            matrix[node[0]][node[1]] = 1
        self.map_matrix = matrix
        return matrix
        # i=0
        # total_num = self.size*self.size - 2
        # block_num = int(self.size*self.size*self.density)
        # while(i<block_num):
        #     target_num = random.randint(1, total_num - i)
        #     #self.print_matrix()
        #     #print (i,target_num,total_num +1 - i)
        #     count = 0
        #     finish_flag = 0
        #     for j in range(self.size):
        #         for k in range(self.size):
        #             if count == target_num:
        #                 if self.map_matrix[j][k] == 1:
        #                     continue
        #                 elif self.map_matrix[j][k] == 0:
        #                     self.map_matrix[j][k] = 1
        #                     finish_flag = 1
        #                     break
        #                 else:#
        #                     print 'error'
        #             if self.map_matrix[j][k] == 0:
        #                 count+=1
        #         if finish_flag == 1:
        #             break
        #     i+=1
        #     finish_flag = 0
        # random.uniform(10, 20)

    def get_matrix(self):
        return self.map_matrix


if __name__ == "__main__":
    print "script_name", sys.argv[0]
    for i in range(1, len(sys.argv)):
        print "argment", i, sys.argv[i]
    print ('start initialize')
    # set the size and density of this matrix
    start = Start(10, 0.3)
    start.print_matrix()
    start.paint_random()
    start.print_matrix()
    print ('start over')
