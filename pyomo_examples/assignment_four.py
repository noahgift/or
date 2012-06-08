"""
Translated problems from Introduction to Management Science:

problem 9.1
problem 9.13
problem 9.20

"""

from coopr.pyomo import (ConcreteModel, Objective, Var, NonNegativeReals,
                              maximize, Constraint)

#Concrete Model
model = ConcreteModel()
#Decision Variables
model.WeeklyProd = Var(Products, within=NonNegativeReals)

#Objective
model.obj = Objective(expr=
            sum(ProfitRate[i] * model.WeeklyProd[i] for i in Products),
            sense = maximize)

def CapacityRule(model, p):
    """User Defined Capacity Rule
    
    Accepts a pyomo Concrete Model as the first positional argument,
    and a list of Plants as a second positional argument
    """
    
    return sum(HoursPerUnit[i,p] * model.WeeklyProd[i] for i in Products) <= HoursAvailable[p]


if __name__ == '__main__':
    #This replicates what the pyomo command-line tools does
    from coopr.opt import SolverFactory
    opt = SolverFactory("glpk")
    instance = model.create()
    results = opt.solve(instance)
    #sends results to stdout
    results.write()
