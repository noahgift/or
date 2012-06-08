"""
Translated problems from Introduction to Management Science:

problem 5.2
problem 5.12
problem 7.4
problem 7.8
problem 7.9

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
