class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        my_dict=defaultdict(int)
        for i in range(len(bills)):
            my_dict[bills[i]]+=1
            if bills[i]==10:
                if my_dict[5]>=1:
                    my_dict[5]-=1
                else:
                    return False
            elif bills[i]==20:
                if my_dict[5]>=1 and my_dict[10]>=1:
                    my_dict[5]-=1
                    my_dict[10]-=1
                elif my_dict[5]>=3:
                    my_dict[5]-=3
                else:
                    return False
        return True

            
        