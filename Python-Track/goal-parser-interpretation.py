class Solution:
    def interpret(self, command: str) -> str:
        l=[]
        for i in range (len(command)):
            if command[i:i+2]=="()":
                l.append("o")
            elif command[i:i+4]=="(al)":
                l.append("al")
            elif command[i]=="G":
                l.append("G")
            else:
                continue
        command=''.join(l)
        return command



            
        