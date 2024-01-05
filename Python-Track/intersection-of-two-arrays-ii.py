class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        if len(nums2)<len(nums1):
            for i in nums2:
                if i in nums1:
                    l.append(i)
                    nums1.remove(i)
        else:
            for i in nums1:
                if i in nums2:
                    l.append(i)
                    nums2.remove(i)
            
        return l
    
        