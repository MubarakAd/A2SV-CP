class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minn=float("inf")
        left=0
        right=k-1
        my_dict=defaultdict(int)
        for i in range(k):
            if blocks[i]=="W":
                my_dict[blocks[i]]+=1
        minn=min(minn,sum(my_dict.values()))
        print(minn)
        while right<len(blocks)-1:
            if blocks[left]=="W":
                my_dict[blocks[left]]-=1
                left+=1
                right+=1
                if blocks[right]=="W":
                   my_dict[blocks[right]]+=1
            else:
                left+=1
                right+=1
                if blocks[right]=="W":
                   my_dict[blocks[right]]+=1

            minn=min(minn,sum(my_dict.values()))
            print(minn)
        return minn


        