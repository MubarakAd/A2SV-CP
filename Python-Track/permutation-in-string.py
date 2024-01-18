class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        my_dict=Counter(s1)
        left=0
        right=len(s1)-1
        my_window=Counter(s2[:right+1])
        while right<len(s2):
            if my_dict==my_window:
                return True
            else:
                my_window[s2[left]]-=1
                left+=1 
                right+=1
                if right==len(s2):
                    break
                my_window[s2[right]]+=1
        return False



        