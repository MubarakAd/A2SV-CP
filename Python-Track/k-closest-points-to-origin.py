class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        my_dic=defaultdict(list)
        my_list=[]
        w=0
        for x,y in points:
            l=[]
            z=math.sqrt((x**2)+(y**2))
            l.append(x)
            l.append(y)
            if z not in my_dic:
                my_dic[z].extend(l)
            else:
                w+=0.00000001
                z+=w
                my_dic[z].extend(l)
        my_dic=dict(sorted(my_dic.items()))
        for i in my_dic:
            k-=1
            my_list.append(my_dic[i])
            if k==0:
                break
        return my_list
        
        
            
        