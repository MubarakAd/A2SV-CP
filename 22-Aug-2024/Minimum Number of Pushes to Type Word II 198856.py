# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        ls =sorted([(v,k) for k,v in counter.items()],reverse = True)
        ans = 0
        k = 1
        ct = 1
        
        for v,_ in ls:
            ans += (ct*v)
            k += 1
            if k > 8:
                k = 1
                ct += 1

        return ans