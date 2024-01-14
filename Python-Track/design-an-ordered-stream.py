class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None] * n 
        self.ptr = 0  

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1  
        self.stream[idKey] = value  
        if idKey == self.ptr:
            chunk = []
            while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
                chunk.append(self.stream[self.ptr])
                self.ptr += 1
            return chunk
        else:
            return []  