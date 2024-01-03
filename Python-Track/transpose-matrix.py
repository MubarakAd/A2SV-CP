class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose=[list(i) for i in zip(*matrix)]
        return transpose
                
        