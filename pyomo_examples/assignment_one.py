"""
Translated problems from Introduction to Management Science:

problem 3.1
problem 3.2
problem 3.6
problem 4.1
problem 4.8

"""
from coopr.pyomo import (ConcreteModel, Objective, Var, NonNegativeReals,
                              maximize, Constraint)






if __name__ == '__main__':
    #This replicates what the pyomo command-line tools does
    from coopr.opt import SolverFactory
    opt = SolverFactory("glpk")
    instance = model.create()
    results = opt.solve(instance)
    #sends results to stdout
    results.write()
