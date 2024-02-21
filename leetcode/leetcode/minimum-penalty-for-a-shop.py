class Solution:
    def bestClosingTime(self, customers: str) -> int:
        lst_nums=[]
        my_dict=defaultdict(int)
        min_penality=float("inf")
        count=0
        l=[]
        val=0
        for i in customers:
            if i=="Y":
                lst_nums.append(1)
            else:
                lst_nums.append(0)
        _sum=0
        pref=[0]*len(lst_nums)
        for i in range(len(pref)):
            _sum+=lst_nums[i]
            pref[i]=_sum
        for i in range(len(pref)):
            if (_sum-(pref[i]-lst_nums[i])+count)<min_penality:
                min_penality=_sum-(pref[i]-lst_nums[i])+count
                l.append(i)
            if customers[i]=="N":
                count+=1
        if count<min_penality:
            l.append(len(pref))
        return l[-1]
       

        
        