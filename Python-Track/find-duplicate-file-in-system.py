class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic={}
        ans=[]

        for path in paths:
            lists= path.split()
           
            for i in range (1,len(lists)): 
                x,y= lists[i].split('.') 

                dic.setdefault(lists[i][len(x)+5:len(lists[i])-1], [])                
                dic[lists[i][len(x)+5:len(lists[i])-1]].append(lists[0]+'/'+lists[i][0:len(x)+4])

       
                
        
        for key in dic:
            if len(dic[key])>1:
                ans.append(dic[key])
        return ans