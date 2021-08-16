
class HashTable:
    def __init__(self):
        self.MAX = 5
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]


t = HashTable()
t['apple'] = 1
t['banana'] = 3
t['Mango'] = 9
t['Peach'] = 5
t['Pineapple'] = 7

print(t.arr)

