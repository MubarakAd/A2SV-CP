class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l=[]
        for i in range(len(boxes)):
            _sum=0
            for j in range(len(boxes)):
                if boxes[j]=="1":
                    _sum+=abs(j-i)
            l.append(_sum)
        return l
        