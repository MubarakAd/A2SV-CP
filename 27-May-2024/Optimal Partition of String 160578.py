# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        hash=defaultdict(set)
        ptr=0
        for i in range(len(s)):
            if s[i] not in hash[ptr]:
                hash[ptr].add(s[i])
            else:
                ptr+=1
                hash[ptr].add(s[i])
        print(hash)
        return len(hash)

            
        