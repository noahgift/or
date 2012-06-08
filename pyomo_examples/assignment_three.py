"""
Translated problems from Introduction to Management Science:

problem 6.1
problem 6.3
problem 6.12
problem 8.6
problem 8.17

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
