class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        my_dict=defaultdict(int)
        count=0
        for i in s:
            if i=="(":
                my_dict[i]+=1
            else:
                if my_dict["("]>=1:
                    my_dict["("]-=1
                else:
                    count+=1
        return count+my_dict["("]
