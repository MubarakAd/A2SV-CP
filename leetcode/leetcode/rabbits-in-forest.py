class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers=Counter(answers)
        num_rabbit=0
        for val,freq in answers.items():
                mult=math.ceil(freq/(val+1))
                num_rabbit+=(mult*(val+1))
        return num_rabbit
       

        