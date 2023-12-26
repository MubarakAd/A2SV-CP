class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minn=float('inf')
        ans=""
        flag=False
        if len(strs)==1:
            return ''.join(strs)
        for i in strs:
            minn=min(len(i),minn)
        for i in range(minn):
            for j in range(len(strs)-1):
                if strs[j][i]==strs[j+1][i]:
                    flag=True
                else:
                    flag=False
                    break
            if flag:
                ans+=strs[j][i]
            else:
                break
        return ans
