class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        my_dict=defaultdict(int)
        for_check=set(nums)
        store=set()
        # count=set()
        right=left=count=0
        while right<len(nums):
            store.add(nums[right])
            my_dict[nums[right]]+=1
            # if store ==for_check:
            while store==for_check:
                count+=(len(nums)-(right))
                print(store,for_check,count)
                print(count)
                my_dict[nums[left]]-=1
                if my_dict[nums[left]]<=0:
                    store.discard(nums[left])
                # if left == right:
                #     left+=1
                #     # right = left
                #     print(store, right)
                left+=1
            right+=1
        return count


        