class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        my_dict=defaultdict(int)
        maxx=float("-inf")
        right=left=0
        while right<len(fruits):
            my_dict[fruits[right]]+=1
            if len(my_dict)<=2:
                right+=1
            else:
                while len(my_dict)>2:
                    my_dict[fruits[left]]-=1
                    if my_dict[fruits[left]]==0:
                        my_dict.pop(fruits[left])
                    left+=1
                right+=1
            maxx=max(maxx,right-left)
        return maxx





        