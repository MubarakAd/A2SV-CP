class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda item:item[1])
        arrow=i=j=0
        while i<len(points):
            if points[i][1]>=points[j][0]:
                while j<len(points)and points[i][1]>=points[j][0]:
                    j+=1
                print(arrow)
            i=j
            arrow+=1
        return arrow  