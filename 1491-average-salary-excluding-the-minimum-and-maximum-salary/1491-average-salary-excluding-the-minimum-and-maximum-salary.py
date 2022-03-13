class Solution:
    def average(self, salary: List[int]) -> float:
        counter = len(salary)
        total_salary = 0
        for val in salary:
            total_salary +=val
        avg_salary = (total_salary - (max(salary)+min(salary)))/ (counter-2)
        return avg_salary
        