class Solution:
    def circularArrayLoop(self,nums):
        def helperFunction(i):
            return (i + nums[i]) % len(nums)
        
        for i, num in enumerate(nums):
            slow = i
            fast = i
            while nums[slow] * nums[helperFunction(fast)] > 0 and nums[slow] * nums[helperFunction(helperFunction(fast))] > 0:
                slow = helperFunction(slow)
                fast = helperFunction(helperFunction(fast))
                if slow == fast:
                    if slow == helperFunction(slow):
                        break
                    return True
        return False