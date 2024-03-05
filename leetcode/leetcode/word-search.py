class Solution:
    def __init__(self):
        self.visited=set()
        self.cells=[]
    def travel(self,letters,x,y):
        if not letters:
            return True
        if not (0 <= x <len(self.cells) and (0 <= y <len(self.cells[0]))):
            return False
        if (x,y) in self.visited or letters[0] !=self.cells[x][y]:
            return False
        self.visited.add((x,y))
        letters =letters[1:]
        res=(self.travel(letters,x+1,y)or 
        self.travel(letters,x-1,y)
        or self.travel(letters,x,y+1)
        or self.travel(letters,x,y-1)
        )
        self.visited.remove((x,y))
        return res
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.cells=board.copy()
        for i in range(len(board)):
            for y in range(len(board[0])):
                if word[0]==board[i][y]:
                    if self.travel(word,i,y):
                        return True
        return False
        


        