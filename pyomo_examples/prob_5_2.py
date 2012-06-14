"""
Resource Usage per Unit of Each Acvity
"""

from coopr.pyomo import (ConcreteModel, Objective, Var, NonNegativeReals,
                              maximize, Constraint)



Activities = ['ActivityOne', 'ActivityTwo'] #Products in other models
UnitProfit = {'ActivityOne':2, 'ActivityTwo':5} #Also called ProfitRate
Resources = ['ResourceOne', 'ResourceTwo']
ResourcesAvailable = {'ResourceOne':10, 'ResourceTwo':12}
ResourcesPerUnit = {('ActivityOne', 'ResourceOne'):1,
                    ('ActivityTwo', 'ResourceOne'):2,
                    ('ActivityOne', 'ResourceTwo'):1,
                    ('ActivityTwo', 'ResourceTwo'):3}

#Concrete Model
model = ConcreteModel()
#Decision Variables
model.Prod = Var(Activities, within=NonNegativeReals)

#Objective
model.obj = Objective(expr=
            sum(UnitProfit[i] * model.Prod[i] for i in Activities),
            sense = maximize)

def ActivityRule(model, r):
    return sum(ResourcesPerUnit[i,r] * model.Prod[i] for i in Activities) <= ResourcesAvailable[r]

model.Utilization = Constraint(Resources, rule = ActivityRule)

#This is an optional code path that allows the script to be run outside of
#pyomo command-line. For example: python wyndor.py
if __name__ == '__main__':
   
   from coopr.opt import SolverFactory
   opt = SolverFactory("glpk")
   instance = model.create()
   results = opt.solve(instance)
   #sends results to stdout
   results.write()

   instance.load(results)  # so we can access variable values by name
   print "Now, we will just write a report (but an ugly one), rather than all results."
   print "we will do it three different ways."
   print "----------"

   print "instance.Prod['ActivityOne'].value=",instance.Prod['ActivityOne'].value
   print "instance.Prod['ActivityTwo'].value=",instance.Prod['ActivityTwo'].value

   for i in instance.Prod:
      print instance.Prod[i], instance.Prod[i].value

   for v in instance.active_components(Var):
      print "Variable",v
      varobject = getattr(instance, v)
      for index in varobject:
         print "   ",index, varobject[index].value
