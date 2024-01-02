class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i]=str(digits[i])
        my_list=list(str(int(''.join(digits))+1))
        for i in range(len(my_list)):
            my_list[i]=int(my_list[i])
        return my_list
      
        
        