
from collections import defaultdict


class Graph:
    # Graph is initialised using default dict
    def __init__(self):
        self.grp = defaultdict(list)
    
    
    # Edge added as key, value pair as a directed Graph
    def add_edge(self, vertex, edge):
        self.grp[vertex].append(edge)
      
    
    # Remove given Edge by New Edge 
    def replace(self, vertex, edge, newEdge):
        for k, v in self.grp.items():
            if k == vertex:
                if edge in v:
                    self.grp[k][self.grp[k].index(edge)] = newEdge
                
    
    # bfs search on Graph returning level of each vertex
    def bfs(self, parent, level):
        flag = 1
        lev = 0 
        level[1] = lev
        while flag:
            flag = 0
            for i in range(1, 101):
                if level[i] == lev:
                    flag = 1
                    temp = self.grp[i]
                    par = i
                for x in temp:
                    if level[x] != -1:
                        continue
                    level[x] = lev+1
                    parent[x] = par
            lev += 1
        return parent, level
        


def main():
    T = int(raw_input())
    for a0 in range(T):
        g = Graph()
        '''
            Graph has following pattern:
            1 -> {2, 3, 4, 5, 6, 7}
            2 -> {3, 4, 5, 6, 7, 8}
            ..
            ...
            94 -> {95, 96, 97, 98, 99, 100}
            95 -> {96, 97, 98, 99, 100}
            ...
            99 ->{100}
        '''
        for i in range(1,101):
            j = 1
            while 1<=j<=6 and j+i<=100: 
                g.add_edge(i, i+j)
                j += 1
       '''
            If stairs are added from a->b then from each 
            vertex replace a->b.Example:A stair is added from 9->27
            then start from 9-6 = 3 and replace a with b
            
            3 -> {4, 5, 6, 7, 8, 27}
            4 -> {5, 6, 7, 8, 27, 10}
            5 -> {6, 7, 8, 27, 10, 11}
       
       '''
        num_stairs = int(raw_input())
        for i in xrange(num_stairs):
            a, b = raw_input().strip().split(' ')
            a, b = int(a), int(b)
            j = a-6
            if j<1: 
                j = 1
            for x in range(j, a):
                g.replace(j, a, b)
       '''
            Similarly like stairs, if a snake is encountered remove that vertex
            from adjacent 6 nodes.Example:A snake is added from 87->34 then loop 
            start from 87-6=81
            
            81 -> {82, 83, 84, 85, 86, 34}
            82 -> {83, 84, 85, 86, 34, 87}
       '''     
        num_snakes = int(raw_input())
        for i in xrange(num_snakes):
            a, b = raw_input().strip().split(' ')
            a, b = int(a), int(b)
            
            j = a-6
            if j<0:
                j=0
            for x in range(j, a, b):
                g.replace(j, a, b)
        

        parent = [0]*101
        
        # Initial level of each edge is -1
        level = [-1]*101
        parent, level = g.bfs(parent, level)

        print level[100]
        
        
        
if __name__=="__main__":
    main()
    
