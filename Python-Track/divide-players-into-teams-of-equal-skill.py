class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left=0
        right=len(skill)-1
        _sum=0
        skill.sort()
        if len(skill)==2:
            return skill[left]*skill[right]
        while left<right:
            if skill[left]+skill[right]!=skill[left+1]+skill[right-1]:
                return -1
            else:
                _sum+=(skill[left]*skill[right])
                left+=1
                right-=1
        return _sum
        