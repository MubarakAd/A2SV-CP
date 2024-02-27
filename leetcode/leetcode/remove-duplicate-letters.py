class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
            my_dict=Counter(s)
            stack=[]
            my_set=set()
            for i in range(len(s)):
                my_dict[s[i]]-=1
                if len(stack)!=0:
                    if stack[-1]<s[i] and s[i] not in my_set:
                        stack.append(s[i])
                        my_set.add(s[i])
                    else:
                        while stack and stack[-1] > s[i] and my_dict[stack[-1]]>0 and s[i] not in my_set :
                            x=stack.pop()
                            my_set.discard(x)
                        if s[i] not in my_set:    
                            stack.append(s[i])
                            my_set.add(s[i])
                else:
                    stack.append(s[i])
                    my_set.add(s[i])
            return ''.join(stack)
        