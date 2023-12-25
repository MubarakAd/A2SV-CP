class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
        my_dic=Counter(arr)
        for i in my_dic:
            if my_dic[i]>len(arr)//4:
                return i
                break