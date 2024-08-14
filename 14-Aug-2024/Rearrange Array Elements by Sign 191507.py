# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=[]
        p=[]
        for i in  nums:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        
        ans=[]
        j=k=0
        for i in range(len(nums)):
            if i%2==0:
                ans.append(p[j])
                j+=1
            else:
                ans.append(n[k])
                k+=1
        return ans

        