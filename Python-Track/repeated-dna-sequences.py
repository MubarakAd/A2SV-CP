class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left=0
        right=10
        ans=[]
        my_dict=defaultdict(int)
        if len(s)<10:
            return []
        while right<len(s)+1:
            my_dict[s[left:right]]+=1
            left+=1
            right+=1
        for i in my_dict:
            if my_dict[i]>=2:
                ans.append(i)
        return ans
            

        