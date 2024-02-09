class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        transpose = list(zip(*board))
        for i in board:
            for j in range(len(i)):
                if i[j].isnumeric() and i.count(i[j]) >1:
                    return False
        for i in transpose:
            for j in range(len(i)):
                if i[j].isnumeric() and i.count(i[j]) > 1:
                    return False
        boxes = []
        for i in range(0, 9, 3):
            box = []
            for j in range(9):
                for k in range(i, i+3):
                    box.append(board[k][j])
                if len(box) == 9:
                    boxes.append(box)
                    box = []

        for i in boxes:
            for j in range(len(i)):
                if i[j].isnumeric() and i.count(i[j]) > 1:
                    return False
        return True
        