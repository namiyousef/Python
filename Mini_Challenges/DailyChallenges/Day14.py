"""
Author: Yousef Nami
Problem definition: the UK has a system of giving loans to it's students. I wanted to understand this and implement
a function that can calculate how much a student has to pay in total based on their salaries.

This is more a finance exercise than it is a coding one, but I was curious so I thought it's worth a try.

Date started: 09.11.2020
Date complete: 
Comments:
    - added an introduction to the actual setup
    - need to add more 
"""


class StudentPlan:
    thresholds = [1615, 2214, 1750]
    interests = [1.1, 2.6, 5.6] # note that for Plan 2, it should increase when income > ~ 27k
    over_threshold_payment = [9, 9, 6]
    
    def __init__(self, Plan=None):
        self.StudyDates = []
        self.StudyFees = []
        self.Plan = Plan if Plan else input("Please enter your plan: ")
        if not isinstance(self.Plan, int) and self.Plan not in 'Pp':
            raise TypeError(
                ("Please enter either 1,2 or P for Postgraduate."
                 "You can visit https://www.gov.uk/repaying-your-student-loan/which-repayment-plan-you-are-on"
                 "to find out which plan you'e on.") 
                )
        i = 1
        print(
            ("This section will ask you about your tuition."
             " You will be asked a series of questions about your fees."
             " If you wish to exit at any point please enter N.")
            )
        while True:
            fee = input("Please enter your Year {} fees: ".format(i))
            if fee == 'N':
                break
            else:
                try:
                    self.StudyFees.append(float(fee))
                except:
                    print("Please enter a number")
                    i -= 1
                    pass
                
                i+=1
            
a = StudentPlan()

print(a.StudyFees)