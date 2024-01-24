class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        new_array=[0]*(len(s)+1)
        for l,r,d in shifts:
            if d==0:
                new_array[l]-=1
                new_array[r+1]+=1
            else:
                 new_array[l]+=1
                 new_array[r+1]-=1
                
        _sum=0
        res=[]
        for i in range(len(s)):
            _sum+=new_array[i]
            new_array[i]=_sum
            new_chr_ascii = (ord(s[i]) - ord("a") + new_array[i]) % 26 + ord("a")
            res.append(chr(new_chr_ascii))
        return "".join(res)
        