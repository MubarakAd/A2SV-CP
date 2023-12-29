class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1="qwertyuiopQWERTYUIOP"
        r2="asdfghjklASDFGHJKL"
        r3="zxcvbnmZXCVBNM"
        ans=[]
        for i in range(len(words)):
            if len(words[i])==1:
                ans.append(words[i])
            else:
                left=0
                right=1
                while right<=len(words[i])-1:
                    if words[i][left] in r1 and words[i][right] in r1:
                        right+=1
                        left+=1
                    elif words[i][left] in r2 and words[i][right] in r2:
                        right+=1
                        left+=1
                    elif words[i][left] in r3 and words[i][right] in r3:
                        right+=1
                        left+=1
                    else:
                        right-=1
                        break
                if right==len(words[i]):
                    ans.append(words[i])
        return ans