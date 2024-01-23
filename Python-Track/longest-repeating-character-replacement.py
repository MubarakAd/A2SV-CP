class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict=defaultdict(int)
        left=right=0
        maxx=0
        longest=0
        while right<len(s):
            my_dict[s[right]]+=1
            maxx=max(my_dict[s[right]],maxx)
            if (right-left+1)-maxx<=k:
                right+=1
            else:
                while (right-left+1)-maxx>k:
                    my_dict[s[left]]-=1
                    left+=1
                right+=1
            longest=max(longest,right-left)
        return longest


        
        