class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l=[]
        my_dic={heights[i]:names[i] for i in range(len(names))}
        my_dic=dict(sorted(my_dic.items(),reverse=True))
        for i in my_dic:
            l.append(my_dic[i])
        return l
        