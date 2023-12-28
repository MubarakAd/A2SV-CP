class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        difff=0
        _zero=0
        _first=0
        result=0

        for i in range(len(points)-1):
            _zero=abs(points[i+1][0]-points[i][0])
            _first=abs(points[i+1][1]-points[i][1])
            if _zero==0:
                result+=_first
            elif _first==0:
                result+=_zero
            else:
                minn=min(_zero,_first)
                minn+=abs(_zero-_first)
                result+=minn
        return result
        