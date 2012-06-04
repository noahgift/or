"""Wyndor model from Hillier and Hillier *Introduction to Management Science*

One way to do it...
Original Author dlw
Modified ndg 

To run this you need pyomo and the glpk solver installed, and need to be
inside of the virtual environment.
When these dependencies are installed you can solve this way (glpk is default):
    
    pyomo wyndor.py

"""

#Explicit importing makes it more clear what a user needs to define
#versus what is included within the pyomo library
from coopr.pyomo import (ConcreteModel, Objective, Var, NonNegativeReals,
                              maximize, Constraint)

Products = ['Doors', 'Windows']
ProfitRate = {'Doors':300, 'Windows':500}
Plants = ['Door Fab', 'Window Fab', 'Assembly']
HoursAvailable = {'Door Fab':4, 'Window Fab':12, 'Assembly':18}
HoursPerUnit = {('Doors','Door Fab'):1, ('Windows', 'Window Fab'):2,
                ('Doors','Assembly'):3, ('Windows', 'Assembly'):2,
                ('Windows', 'Door Fab'):0, ('Doors', 'Window Fab'):0}

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

#This statement is what pyomo needs to solve
model.Capacity = Constraint(Plants, rule = CapacityRule)

#This is an optional code path that allows the script to be run outside of
#pyomo command-line.  For example:  python wyndor.py
if __name__ == '__main__':
   
    #This replicates what the pyomo command-line tools does
    from coopr.opt import SolverFactory
    opt = SolverFactory("glpk")
    instance = model.create()
    results = opt.solve(instance)
    #sends results to stdout
    results.write()

