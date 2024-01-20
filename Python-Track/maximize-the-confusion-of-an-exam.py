class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        my_dict=defaultdict(int)
        right=0
        left=0
        longest=float("-inf")
        count=0
        while right<len(answerKey):
            my_dict[answerKey[right]]+=1
            if my_dict["F"]<=k or my_dict["T"]<=k:
                right+=1
            else:
                while my_dict["F"]>k and my_dict["T"]>k:
                    my_dict[answerKey[left]]-=1
                    left+=1
                right+=1
            longest=max(longest,right-left)
        return longest
                     
            

