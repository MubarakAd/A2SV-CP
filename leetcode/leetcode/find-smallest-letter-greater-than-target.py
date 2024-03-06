class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left,right=0,len(letters)-1
        min_let="#"
        while left<=right:
            mid=(right+left)
            if letters[mid]>target:
                min_let=letters[mid]
                right=mid-1
            else:
                left=mid+1
        if min_let=="#":
            return letters[0]
        return min_let
            
        