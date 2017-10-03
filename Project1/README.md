INTRO TO ARTIF INTEL 520
# PROJECT1 MAZE GAME
by Wenzhong Li  |  Heng-Shao Chen  | Juntao Tan  |  Yingqiang Ge
## Algorithm
### DFS
Include two Python file, DFS.py and DFS_optimal.
DFS.py is an implement of Breadth-first search. Only find the first path from start node to the end node.
DFS_optimal.py is an implement of Breadth-first search. Will keep running until find the shortest route.
### BFS
BFS.py is an implement of Depth-first search. Always finds the shortest path when it finish.
### A*
A* is a modification of UFCS Algorithm that is optimized for a single destination.
UFCS Algorithm can find paths to all locations; A* finds paths to one location.
It prioritizes paths that seem to be leading closer to the goal.
ASTAR_EUC.py is an implement of A* using Euclidean Distance.
ASTAR_MHT.py is an implement of A* using Manhattan Distance.
### Genetic Algorithm
A genetic algorithm (GA) is a meta-heuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA).
Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on bio-inspired operators such as mutation, crossover and selection.
See Genetic Script chapter for more GA Script detail.
### Simulated Annealing
SA is a general-purpose, serial algorithm for finding a global minimum for a
continuous function. It is also a popular Monte Carlo algorithm for any optimization
problem including COPs. The solutions by this technique are close to the global
minimum within a polynomial upper bound for the computational time and are
independent of the initial conditions. Some parallel algorithms for SA have been
proposed aiming to improve the accuracy of the solutions by applying parallelism
SimAnealing.py is an implement of Simulated Annealing.
## Maze Generator
### Start
Start.py provide random algorithm to build a random maze with set p and size.
## Statistics Script
### Question 1
Question1.py run all 4 Algorithm on the same solvable maze.
From p = 0.0 to p = 4.0, run them all on stet of increasing size of maze, starting at 10*10.
Whenever there is a algorithm exceeded 60 seconds, end of Script.
### Question 2
Question2 file include visualization by HTML and Python Script.
Question2.py is a data generate Script.
First it generate a random solvable maze with requested size.
Then, run all 4 algorithm on this maze.
At last, print the solutions and save it to data.js file.
Visualization is built by HTML5UP frame.
See Visualization chapter for more visualization detail.
### Question 3
Question3.py run DFS algorithm to determine if this map has a solution.
This Script will run from p = 0.0 to p = 1.0.
However, there usually no solvable maze when maze is randomly generated with p above 0.4.
So this Script will coming to a stop when p is over 0.43.
And run 100 times to see how many percentage mazes are solvable.
### Question 4
Question4.py run BFS algorithm to find the average length of the shortest path.
Also run DFS on this to show what other path distance is.
This Script will run from p = 0.0 to p = 0.4.
And run 100 times to  get the average.
### Question 5
Question5.py run A* Manhattan Distance algorithm to find the average length of path.
Also run DFS on this to compare with it.
This Script will run from p = 0.0 to p = 0.4.
And run 32 times to  get the average.
### Question 6
Question6.py run A* Manhattan Distance and A* using Euclidean Distance algorithm to find the average number of nodes expanded in total for a random map.
This Script will run from p = 0.0 to p = 0.4.
And run 100 times to  get the average.
### Question 7 BFS/DFS
Question7_BFS.py run BFS algorithm to determine if this map has a solution.
If it is solvable, find the average number of nodes expanded in total for a random map.
This Script will run from p = 0.0 to p = 0.4.
And run 100 times to  get the average.
Question7_DFS.py using DFS algorithm to determine if this map has a solution.
If it is solvable, find the average number of nodes expanded in total for a random map.
This Script will run from p = 0.0 to p = 0.4.
And run 100 times to  get the average.
## Visualization
### index.html
index.html is a HTML with JavaScript.
JavaScript will read the data.js file and show the result in web page.
Please double click the index.html and check out the web page~
### data.js
Contain data in JSON form. Import to HTML file as a "*.js" file.
Data include the original map and the solution provided by all 4 algorithm.
## Genetic Script
### GA DFS
Contain three files GA_DFS_FRINGE.py, GA_DFS_Length.py and GA_DFS_NODES.py.
GA_DFS_FRINGE.py generates maze has the longest solution path returned.
GA_DFS_FRINGE.py generates maze has the biggest total number of nodes expanded.
GA_DFS_NODES.py generates maze has the maximum size of fringe during runtime.
### GA BFS
Contain three files GA_BFS_FRINGE.py, GA_BFS_Length.py and GA_BFS_NODES.py.
GA_BFS_FRINGE.py generates maze has the longest solution path returned.
GA_BFS_FRINGE.py generates maze has the biggest total number of nodes expanded.
GA_BFS_NODES.py generates maze has the maximum size of fringe during runtime.
### GA A*
Contain six files GA_ASTAR_MHT_FRINGE.py, GA_ASTAR_MHT_LENGTH.py, GA_ASTAR_MHT_NODES.py, GA_ASTAR_EUC_FRINGE.py, GA_ASTAR_EUC_LENGTH.py and GA_ASTAR_EUC_NODES.py.
GA_ASTAR_MHT_LENGTH.py generates maze has the longest solution path returned.
GA_ASTAR_MHT_NODES.py generates maze has the biggest total number of nodes expanded.
GA_ASTAR_MHT_FRINGE.py generates maze has the maximum size of fringe during runtime.
GA_ASTAR_EUC_LENGTH.py generates maze has the longest solution path returned.
GA_ASTAR_EUC_NODES.py generates maze has the biggest total number of nodes expanded.
GA_ASTAR_EUC_FRINGE.py generates maze has the maximum size of fringe during runtime.
