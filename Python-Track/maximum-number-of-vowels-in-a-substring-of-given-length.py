class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        my_dic=defaultdict(int)
        my_set={"a","e","i","o","u"}
        count=0
        for i in range(k):
            if s[i] in my_set:
                my_dic[s[i]]+=1
                count+=1
        right=k
        left=0
        maxx=count
        if k==len(s)-1:
            return count
        print(len(s),count)
        while right<len(s):
            if s[left] in my_set:
                my_dic[s[left]]-=1
                count-=1
            if s[right] in my_set:
                my_dic[s[right]]+=1
                count+=1
            right+=1
            left+=1
            maxx=max(count,maxx)
        return maxx
            
        