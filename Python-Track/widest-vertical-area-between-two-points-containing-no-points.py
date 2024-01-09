class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxx=float("-inf")
        points.sort()
        for i in range(len(points)-1):
            maxx=max(maxx,abs(points[i][0]-points[i+1][0]))
        return maxx

        