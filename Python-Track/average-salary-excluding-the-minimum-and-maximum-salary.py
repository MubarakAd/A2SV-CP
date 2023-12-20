class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        l=sum(salary)/len(salary)
        result="{:.5f}".format(l)
        return float(result)
        