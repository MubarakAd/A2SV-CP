class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        left=0
        right=0
        i=0
        my_dic={order[i]:i for i in range(len(order))}
        while i<len(words)-1:
            if words[i]==words[i+1]:
                i+=1
            elif left>len(words[i])-1:
                i+=1
            elif right>len(words[i+1])-1:
                return False
            elif my_dic[words[i][left]]<my_dic[words[i+1][right]]:
                i+=1
            elif my_dic[words[i][left]]==my_dic[words[i+1][right]]:
                right+=1
                left+=1
            else:
                return False
        return True
