class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left=0
        right=len(people)-1
        people.sort()
        _sum=0
        if len(people)==1:
            return 1
        while right>=left:
            if people[right]+people[left]<=limit:
                right-=1
                left+=1
                _sum+=1
            elif people[right]<=limit:
                _sum+=1
                right-=1
        return _sum