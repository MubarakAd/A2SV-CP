class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
            Even_sum=0
            ans=[]
            for i in nums:
                if i%2==0:
                    Even_sum+=i
            for x,y in queries:
                if (nums[y]+x)%2==0:
                    if nums[y]%2==0:
                        Even_sum-=nums[y]
                        Even_sum+=(nums[y]+x)
                        nums[y]=nums[y]+x
                        ans.append(Even_sum)
                    else:
                        Even_sum+=(nums[y]+x)
                        nums[y]=nums[y]+x
                        ans.append(Even_sum)
                else:
                    if nums[y]%2==0:
                        Even_sum-=nums[y]
                        nums[y]=(nums[y]+x)
                        ans.append(Even_sum)
                    else:
                        ans.append(Even_sum)
                        nums[y]=(nums[y]+x)
            return ans