class Pair:

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:

    def __init__(self):
        self.total_size = 2
        self.current_capacity = 0
        self.map: [Pair] = [Pair(None, None)] * self.total_size

    def insert(self,  key, value):
        hashed_key = self.__hash(key)
        while True:
            if self.map[hashed_key].key is None:
                self.map[hashed_key] = Pair(key, value)
                self.current_capacity += 1
                if self.current_capacity >= self.total_size/2:
                    self.rehash()
                return
            else:
                if self.map[hashed_key].key == key:
                    self.map[hashed_key] = Pair(key, value)
                    return
            hashed_key += 1
            hashed_key %= self.total_size

    def get(self, key):
        hashed_key = self.__hash(key)
        while True:
            if self.map[hashed_key].key is None:
                print('Debug: The Key does not exist')
                return
            else:
                if self.map[hashed_key].key == key:
                    return self.map[hashed_key].value

            hashed_key += 1
            hashed_key %= self.total_size

    def __hash(self, key):
        hashed_key = sum(ord(c) for c in key) % self.total_size
        return hashed_key

    def rehash(self):
        pass
        old_map = self.map
        self.total_size *= 2
        self.map = [Pair(None, None)] * self.total_size
        for pair in old_map:
            if pair.key is not None:
                self.insert(pair.key, pair.value)

if __name__ == '__main__':
    hashMap = HashMap()
    hashMap.insert('rohail', 2)
    hashMap.insert('salatq', 25)
    print(f' Rohail Val {hashMap.get('rohail')}')
    print(f' rohailz Val {hashMap.get('rohailz')}')
    print(f' salatq Val {hashMap.get('salatq')}')
