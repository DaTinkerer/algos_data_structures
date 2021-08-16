
class HashTable:
    # sets an initial array and the size of the array
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self, key):
        h = 0
        for char in key:
            #sums all the ascii codes in each character and sets it to h
            h += ord(char)
        # this gives the key a unique indentifier 
        return h % self.MAX
    # lets me set any value and give it an index in the array
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
    # returns the index of the given key
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]


t = HashTable()
t['apple'] = 1
t['banana'] = 3
t['Mango'] = 9
t['Peach'] = 5
t['Pineapple'] = 7



