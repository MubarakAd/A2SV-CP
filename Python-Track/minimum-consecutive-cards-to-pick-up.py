class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minn=float("inf")
        flag=False
        right=0
        left=0
        my_dict=defaultdict(int)
        while right<len(cards):
            my_dict[cards[right]]+=1
            if my_dict[cards[right]]>=2:
                
                flag=True
                while cards[left]!=cards[right]:
                    my_dict[cards[left]]-=1
                    left+=1
                minn=min(minn,right-left)
                my_dict[cards[left]]-=1
                left+=1
                right+=1
            else:
                right+=1
        if flag:
            return minn+1
        return -1
        