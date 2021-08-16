class UnionFind:
    def __init__(self):

        # Number of elements in the union find
        self.size = int
        # tracks the size of each component
        self.sz = [int]
        # id[i] points to the parent of i, if id[i] = i, then i is a root node
        self.id = [int]
        # Number of componenents in union find
        self.num_components = int

    def union_find(self, size):
        if (size <= 0):
            print("size must be greater than 0")
        else:
            self.size = num_components = size
            sz = [size]
            id = [size]

            for i in size:
                id[i] = i # link to itself
            sz[i] = 1 # size of each component is initially 1
    
    # finds which component/set p belongs to.
    def find(self, p):
        # finds the root of the component
        root = p
        while root != [id][root]:
            root = [id][root]
        
        while p != root:
            next = id[p]
            id[p] = root
            p = next



