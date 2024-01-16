class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dic=defaultdict(int)
        longest=0
        left=0
        right=0
        maxx=0
        while right<len(s):
            my_dic[s[right]]+=1
            if my_dic[s[right]]>1:
                while my_dic[s[right]]>1:
                    my_dic[s[left]]-=1
                    left+=1
                right+=1
            else:
                right+=1
            maxx=max(maxx,right-left)
            
        return maxx



        