class Employee:
    def __init__(self, fn, ln, annual_salary):
        self.fn = fn
        self.ln = ln
        self.annual_salary = annual_salary

    def get_raise(self, annual_salary_adds=5000):
        self.annual_salary += annual_salary_adds