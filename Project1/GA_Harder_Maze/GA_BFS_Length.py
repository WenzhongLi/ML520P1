#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Juntao Tan
'''
import Project1.Start
import Project1.BFS
import random
import json
import copy


class GA():
    def __init__(self, size, count,mu_rate):
        self.mu_rate = mu_rate
        # length of per chromosome
        self.size = size
        # num of chromosom
        self.count = count
        # randomly create generation
        self.generation = self.gen_generation(size,count)

    def gen_chromosome(self, size):
        #randomly generate a maze
        maze = Project1.Start.Start(size, 0.3)
        maze.paint_random()
        chromosome = maze.get_matrix() # chromosome is a size x size random matrix
        return chromosome

    def gen_generation(self, size, count):
        # generate the first generation
        #return [self.gen_chromosome(size) for i in range(count)]
        generation = []
        i = 0
        while i < count:
            # del the maze with no solution
            cr = self.gen_chromosome(size)
            if self.fitness(cr) != 0:
                generation.append(cr)
                i += 1
        return generation

    def fitness(self, chromsome):
        bfs = Project1.BFS.BFS()
        res = bfs.bfs_init(chromsome, self.size)
        if res[0] == 1:
            return res[2]
        else:
            return res[0]

    def evolve(self):
        parents = copy.deepcopy(self.selection)
        children = copy.deepcopy(self.crossover(parents))
        self.generation = copy.deepcopy(children)

    @property
    def selection(self):
        # del the mazes with no solution
        #good_generation = []
        #for i in self.generation:
        #    if self.fitness(i) != 0:
        #        good_generation.append(i)
        # count total fitness
        parents = []
        sumfit = 0
        for i in self.generation:
            sumfit = sumfit + self.fitness(i)


        #good_generation = []

        '''
        # del the mazes with no solution
        for i in self.generation:
            if self.fitness(i) != 0:
                good_generation.append(i)
        '''

        # count total fitness
        # print good_generation
        # print len(good_generation)
        sumfit = 0
        for i in self.generation:
            sumfit = sumfit + self.fitness(i)

        # print sumfit
        # pickup parants as the value of fitness(high fitness more possibility)

        for i in range(self.count):
            a = random.randint(0, sumfit)
            j = 0
            while (a - self.fitness(self.generation[j])) > 0:
                a = a - self.fitness(self.generation[j])
                j += 1

            parents.append(self.generation[j])
            #        print a
        # print len(parents)
        return parents



    def crossover(self,parents):

        # even chromosome crossover with next
        step_P = copy.deepcopy(parents) # for first cross
        random_P = copy.deepcopy(parents) # for second cross
        children = []
        best_fit = 0
        for i in parents:
            if self.fitness(i)> best_fit:
                best_fit = self.fitness(i)
        #print 1,best_fit
        for i in range(0,len(step_P),2):
                cros = random.randint(1, self.size - 1)
                temp = [0] * self.size
                # cross
                reserve_parents1 = copy.deepcopy(step_P[i])
                reserve_parents2 = copy.deepcopy(step_P[i+1])
                for j in range(cros, self.size):
                    temp[j] = copy.deepcopy(step_P[i][j])
                    step_P[i][j] = copy.deepcopy(step_P[i+1][j])
                    step_P[i+1][j] = copy.deepcopy(temp[j])
                # put good chromosome to children
                #print i, self.fitness(step_P[i]), i+1, self.fitness(step_P[i+1])

                if self.fitness(reserve_parents1) > self.fitness(step_P[i]):
                    children.append(copy.deepcopy(reserve_parents1))
                else:
                    children.append(copy.deepcopy(step_P[i]))
                    #print i #,self.fitness(step_P[i])
                    #print children
                    # print fit children
                    #fit_children = []
                    #for c in children:
                    #    fit_children.append(self.fitness(c))
                    #print fit_children

                if self.fitness(reserve_parents2) > self.fitness(step_P[i+1]) != 0:
                    children.append(copy.deepcopy(reserve_parents2))
                else:
                    children.append(copy.deepcopy(step_P[i+1]))
                    #print i+1 #,self.fitness(step_P[i+1])
                    #print children
                    #fit_children = []
                    #for c in children:
                    #    fit_children.append(self.fitness(c))
                    #print fit_children

        # make children number to count
        while len(children) < self.count:
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


    def get_optimal_chromesome(self):
        best_chromosome_num = 0  # the best chromosome in the current generation
        best_fit = 0
        for i in range(0, len(self.generation)):
            if self.fitness(self.generation[i]) > best_fit:
                best_fit = self.fitness(self.generation[i])
                best_chromosome_num = i
        return self.generation[best_chromosome_num]



    def result(self):
        res = [0] * 5   #reserve result

        best_chromosome_num = 0    #the best chromosome in the current generation
        best_fit = 0
        for i in range(0, len(self.generation)):
            if self.fitness(self.generation[i]) > best_fit:
                best_fit = self.fitness(self.generation[i])
                best_chromosome_num = i
        bfs = Project1.BFS.BFS()
        res = copy.deepcopy(bfs.bfs_init(self.generation[best_chromosome_num],self.size))
        print res
        return res



        best_fit = 0
        #best_chromosome
        #or i in self.generation:
        #    if self.fitness(i)> best_fit:
        #        best_fit = self.fitness(i)
        #sumfit = 0
        #for i in self.generation:
        #    sumfit = sumfit + self.fitness(i)

        #fit = []
        #for i in self.generation:
        #    fit.append(self.fitness(i))





    def mutation(self, mu_rate):

        for i in range(0, len(self.generation)):
            temp_generation = copy.deepcopy(self.generation)
            if random.random() < mu_rate:
                k = random.randint(0, self.size-1)
                l = random.randint(0, self.size-1)
                temp_generation[i][k][l] = 1
                if self.fitness(temp_generation[i]) != 0:
                    self.generation[i] = copy.deepcopy(temp_generation[i])




if __name__ == "__main__":
    ga = GA(100, 30, 0.3)
    last_result = ga.result()
    rep = 0
    for i in range(100000000):
        ga.evolve()
        result =  ga.result()
        if last_result == result:
            rep += 1
        else:
            rep = 0
        if rep > 20:
            break
        last_result = result
    print ga.get_optimal_chromesome()
        #print rep
    '''
    f1 = open('GA_BFS_Length', 'w')
    data = copy.copy(ga.get_optimal_chromesome())
    json = json.dumps(data)
    f1.write("GA_BFS_Optimal_Length = " + json + ";")
    f1.flush()
    f1.close()
    '''

    f1 = open('GA_OPTIMAL_MAZE/GA_BFS_LENGTH.js', 'w')
    map = copy.copy(ga.get_optimal_chromesome())
    data = dict()
    original = {"size": len(map), "map": map}
    data["original"] = original
    json = json.dumps(data)
    f1.write("var json_data = " + json + ";")
    f1.flush()
    f1.close()
