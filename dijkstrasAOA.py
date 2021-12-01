import tkinter as tk
from tkinter import ttk
from collections import defaultdict
def show_entry_fields():
    
        g = Graph()
        list1=["COLABA","CSMT","CHURCHGATE","MARINE","MALABAR","BYCULLA","MAHALAXMI","CHINCHPOKALI",
              "LALBAUG","WORLI","PAREL","DADAR","MATUNGA","WADALA","MAHIM","SION"]
        graph=[
       [0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   	   [5,0,2,0,0,5,0,0,0,0,0,0,0,0,0,0],
       [0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,2,0,4,4,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,4,0,5,5,0,0,0,0,0,0,0,0,0],
	   [0,5,0,4,5,0,0,2,2,0,0,0,0,0,0,0],
	   [0,0,0,0,5,0,0,2,0,2,0,0,0,0,0,0],
	   [0,0,0,0,0,2,2,0,1,0,0,0,0,0,0,0], 
	   [0,0,0,0,0,2,0,1,0,0,1,0,0,6,0,0],
	   [0,0,0,0,0,0,2,0,0,0,2,5,0,0,0,0],
	   [0,0,0,0,0,0,0,0,1,2,0,2,0,4,0,0],
	   [0,0,0,0,0,0,0,0,0,5,2,0,1,1,3,0],
	   [0,0,0,0,0,0,0,0,0,0,0,1,0,1,2,2],
	   [0,0,0,0,0,0,0,0,6,0,4,1,1,0,0,4],
	   [0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,3],
	   [0,0,0,0,0,0,0,0,0,0,0,0,2,4,3,0],
       ]
        srcval=e1.get().upper()
        destval=e2.get().upper()
        if srcval not in list1 or destval not in list1:
            
            label=tk.Label(master,text="routes not available").grid(row=5)
        else:
            print("Source: %s\nDestination: %s" % (srcval, destval))
            g.dijkstra(graph, srcval,destval)

    
class Graph:

    def minDistance(self, dist, queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1

        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    # Function to print shortest path
    # from source to j
    # using parent array

    def printPath(self, parent, j,gridval):
        
        temp=j
        sourceval = {0: "COLABA",1:"CSMT",2:"CHURCHGATE",3:"MARINE",4:"MALABAR",5:"BYCULLA",6:"MAHALAXMI",7:"CHINCHPOKALI",
                     8:"LALBAUG",9:"WORLI",10:"PAREL",11:"DADAR",12:"MATUNGA",13:"WADALA",14:"MAHIM",15:"SION"}
       
        
        for x,y in sourceval.items():
            if x == j:
                j = y
      
        if parent[temp] == -1:

            label1=tk.Label(master,text="\n%s"%(j)).grid(row=6),
           
            return
        self.printPath(parent, parent[temp],gridval-1)
       
        label2=tk.Label(master,text="\n%s"%(j)).grid(row=gridval),
        
    def printSolution(self, dist, parent, src,dest,temp1):
        print("Vertex \t\tDistance from Source in kms\tPath")
        gridval=13
        if dest == 0:
                i=0
                label = tk.Label(master, text= "\n%s --> %s \t\t%d km\t\t\t\t\t" % (src, temp1, dist[i])).grid(row=5)

                print("\n%s --> %s \t\t%d km\t\t\t\t\t" % (src, temp1, dist[i])),
                self.printPath(parent, i,gridval)
        for i in range(1, len(dist)):
            
            if i == dest:
                
                self.printPath(parent, i,gridval)
                label = tk.Label(master, text= "\n%s --> %s \t\t%d km\t\t\t\t\t" % (src, temp1, dist[i])).grid(row=5)
                print("\n%s --> %s \t\t%d km\t\t\t\t\t" % (src, temp1, dist[i])),

            

    '''Function that implements Dijkstra's single source shortest path
	algorithm for a graph represented using adjacency matrix
	representation'''
    
    def dijkstra(self, graph, src,dest):
        temp=src
        temp1=dest
        sourceval = {0: "COLABA",1:"CSMT",2:"CHURCHGATE",3:"MARINE",4:"MALABAR",5:"BYCULLA",6:"MAHALAXMI",7:"CHINCHPOKALI",
                     8:"LALBAUG",9:"WORLI",10:"PAREL",11:"DADAR",12:"MATUNGA",13:"WADALA",14:"MAHIM",15:"SION"}
        destinationval= {0: "COLABA",1:"CSMT",2:"CHURCHGATE",3:"MARINE",4:"MALABAR",5:"BYCULLA",6:"MAHALAXMI",7:"CHINCHPOKALI",
                     8:"LALBAUG",9:"WORLI",10:"PAREL",11:"DADAR",12:"MATUNGA",13:"WADALA",14:"MAHIM",15:"SION"}
        
        for x,y in sourceval.items():
            if y == src:
                src = int(x)
        for x,y in destinationval.items():
            if y == dest:
                dest = int(x)
        row = len(graph)
        col = len(graph[0])

        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        dist = [float("Inf")] * row

        # Parent array to store
        # shortest path tree
        parent = [-1] * row

         # Distance of source vertex
         # from itself is always 0
        dist[src] = 0

          # Add all vertices in queue
        queue = []
        for i in range(row):
            queue.append(i)

            # Find shortest path for all vertices
        while queue:

                # Pick the minimum dist vertex
                # from the set of vertices
                # still in queue
            u = self.minDistance(dist, queue)

                # remove min element
            queue.remove(u)

                # Update dist value and parent
                # index of the adjacent vertices of
                # the picked vertex. Consider only
                # those vertices which are still in
                # queue
            for i in range(col):
                '''Update dist[i] only if it is in queue, there is 
                    an edge from u to i, and total weight of path from 
                    src to i through u is smaller than current value of 
                    dist[i]'''
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
    
        
            # print the constructed distance array
        self.printSolution(dist, parent, temp,dest,temp1)
        

        



master = tk.Tk()
master.title('Map')

tk.Label(master, text="Source").grid(row=0)
tk.Label(master, text="Destination").grid(row=1)


e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


tk.Button(master, 
          text='Show Shortest Path', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                      pady=4)

master.mainloop()
