class Solution:
    def freqAlphabets(self, s: str) -> str:
        my_dic={
    "1":"a",
    "2":"b",
    "3":"c",
    "4":"d",
    "5":"e",
    "6":"f",
    "7":"g",
    "8":"h",
    "9":"i",
    "10#":"j",
    "11#":"k",
    "12#":"l",
    "13#":"m",
    "14#":"n",
    "15#":"o",
    "16#":"p",
    "17#":"q",
    "18#":"r",
    "19#":"s",
    "20#":"t",
    "21#":"u",
    "22#":"v",
    "23#":"w",
    "24#":"x",
    "25#":"y",
    "26#":"z"
    
        }
        left=0
        right=1
        l=[]
        if len(s)==2:
            l.append(my_dic[s[left]])
            l.append(my_dic[s[right]])
        else:
            while right<=len(s)-1:
                if right==len(s)-1:
                    l.append(my_dic[s[left]])
                    l.append(my_dic[s[right]])
                    left+=2
                    right+=2
                else:
                    if s[right+1]=="#":
                        l.append(my_dic[s[left:right+2]])
                        left=right+2
                        right=left+1
                    else:
                        l.append(my_dic[s[left]])
                        left+=1
                        right+=1
        if left==len(s)-1:
            l.append(my_dic[s[left]])
            left+=1 
        return ''.join(l)