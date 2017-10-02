#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Juntao Tan
'''

import Project1.Start
import Project1.DFS
import copy
import json
import random

class GA():
    # initialize
    def __init__(self, size, count, mu_rate):
        # mutation rate
        self.mu_rate = mu_rate
        # length of per chromosome
        self.size = size
        # num of chromosomes
        self.count = count
        # randomly create generation
        self.generation = self.gen_generation(size, count)

    def gen_chromosome(self, size):
        # randomly generate a maze with a density of 0.3
        maze = Project1.Start.Start(size, 0.3)
        maze.paint_random()
        # chromosome is a size x size random matrix
        chromosome = maze.get_matrix()
        return chromosome


    def gen_generation(self, size, count):
        # generate the first generation

        generation = []
        i = 0
        # generate chromosomes till the number reach the count
        while i < count:
            # del the maze with no solution
            cr = self.gen_chromosome(size)
            # just pick up the chromosomes with solution
            if self.fitness(cr) != 0:
                generation.append(cr)
                i += 1
        return generation

    def fitness(self, chromsome):
        # used to count fitness of each chromosome
        # choose the algorithm used to solve the mazes
        dfs = Project1.DFS.DFS()
        res = dfs.dfs_route(chromsome, self.size)
        # res[0] shows if the chromosome has a solution
        if res[0] == 1:
            # return the value as fitness (res[2] is length, res[3] is the number of extended nodes, res[4] is the number of fringe)
            return res[4]
        else:
            return res[0]


    def reproducing(self):
        # reproduce next generation
        parents = copy.deepcopy(self.selection())
        # children are the next generation
        children = copy.deepcopy(self.crossover(parents))
        self.generation = copy.deepcopy(children)
        self.mutation(self.mu_rate)

    def selection(self):
        # select parents
        parents = []

        # count the total fitness in each generation
        sumfit = 0
        for i in self.generation:
            sumfit = sumfit + self.fitness(i)
        # pickup parants as the value of fitness(high fitness more possibility)
        for i in range(self.count):
            a = random.randint(0, sumfit)
            j = 0
            while (a - self.fitness(self.generation[j])) > 0:
                a = a - self.fitness(self.generation[j])
                j += 1
            parents.append(self.generation[j])
        return parents

    def crossover(self,parents):
        # generate children through crossover
        step_P = copy.deepcopy(parents) # for first step of cross
        random_P = copy.deepcopy(parents) # for second step of cross (randomly choose parents)
        children = []
        best_fit = 0
        '''
        for i in parents:
            if self.fitness(i)> best_fit:
                best_fit = self.fitness(i)
        '''
        # even chromosome crossover with next
        for i in range(0,len(step_P),2):
                cros = random.randint(1, self.size - 1)
                temp = [0] * self.size
                # cross
                reserve_parents1 = copy.deepcopy(step_P[i])
                reserve_parents2 = copy.deepcopy(step_P[i+1])
                # randomly pick up a number to decide the cut position
                for j in range(cros, self.size):
                    temp[j] = copy.deepcopy(step_P[i][j])
                    step_P[i][j] = copy.deepcopy(step_P[i+1][j])
                    step_P[i+1][j] = copy.deepcopy(temp[j])
                # put good chromosome to children
                if self.fitness(reserve_parents1) > self.fitness(step_P[i]):
                    children.append(copy.deepcopy(reserve_parents1))
                else:
                    children.append(copy.deepcopy(step_P[i]))
                if self.fitness(reserve_parents2) > self.fitness(step_P[i+1]):
                    children.append(copy.deepcopy(reserve_parents2))
                else:
                    children.append(copy.deepcopy(step_P[i+1]))
        # fix children number to count
        while len(children) < self.count:
            # randomly pick up parents to crossover in this step
            m = random.randint(0, len(parents)-1)
            n = random.randint(0, len(parents)-1)
            cros = random.randint(1,self. size-1)
            temp = [0]*self.size
            for j in range(cros, self.size):
                temp[j] = random_P[m][j]
                random_P[m][j] = random_P[n][j]
                random_P[n][j] = temp[j]
            if self.fitness(random_P[m]) != 0:
                children.append(random_P[m])
            elif self.fitness(random_P[n])!=0:
                children.append(random_P[n])
        return children

    def result(self):
        # used to reserve the best fitness in current generation
        res = [0] * 5   #reserve result
        best_chromosome_num = 0    #the best chromosome in the current generation
        best_fit = 0
        for i in range(0, len(self.generation)):
            if self.fitness(self.generation[i]) > best_fit:
                best_fit = self.fitness(self.generation[i])
                best_chromosome_num = i
        dfs = Project1.DFS.DFS()
        res = copy.deepcopy(dfs.dfs_route(self.generation[best_chromosome_num],self.size))
        print res
        return res[3]  # the fitness value


    def get_optimal_chromesome(self):
        # used to print the best chromosome in the current generation
        best_chromosome_num = 0  # the best chromosome in the current generation
        best_fit = 0
        for i in range(0, len(self.generation)):
            if self.fitness(self.generation[i]) > best_fit:
                best_fit = self.fitness(self.generation[i])
                best_chromosome_num = i
        return self.generation[best_chromosome_num]


    def mutation(self, mu_rate):
        # for each node in the maze, use mu_rate to decide whether change it or not
        for i in range(0, len(self.generation)):
            temp_generation = copy.deepcopy(self.generation)
            # will change?
            if random.random() < mu_rate:
                k = random.randint(0, self.size-1)
                l = random.randint(0, self.size-1)
                temp_generation[i][k][l] = 1
                if self.fitness(temp_generation[i]) != 0:
                    self.generation[i] = copy.deepcopy(temp_generation[i])

if __name__ == "__main__":
    ga = GA(10, 30, 0.3)
    last_result = ga.result()
    # rep use to count how many generation that do not improve the best fitness
    rep = 0
    # only when the fitness do not improve for 10 steps that the process be terminate
    while 1:
        ga.reproducing()
        result =  ga.result()
        # is the best fitness not improve in next generation?
        # if is, rep + 1
        if last_result <= result:
            rep += 1
        # if not, reset rep
        else:
            rep = 0
        if rep > 20:
            break
        last_result = result
    print ga.get_optimal_chromesome()
    # print the best maze to a js file used to draw the maze
    f1 = open('GA_OPTIMAL_MAZE/GA_DFS_FRINGE.js', 'w')
    map = copy.copy(ga.get_optimal_chromesome())
    data = dict()
    original = {"size": len(map), "map": map}
    data["original"] = original
    json = json.dumps(data)
    f1.write("var json_data = " + json + ";")
    f1.flush()
    f1.close()


