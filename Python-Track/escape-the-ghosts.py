class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        start=[0,0]
        flag=False
        my_sample=abs(target[0]-start[0])+abs(target[1]-start[1])
        for i,j in ghosts:
            g_step=abs(i-target[0])+abs(j-target[1])
            if my_sample>=g_step:
                flag=True
                break
        if flag:
            return False
        else:
            return True
        