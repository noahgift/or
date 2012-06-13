#Credit to Andriy Mysyk 06/01/2012

from coopr.pyomo import *

# create a model root
model = AbstractModel()

# set bounds:
# n - number of nodes
# max_out - number of arcs out of each node
# max_in - number of arcs in each node
# arc_to_self - number of arcs to self allowed
# min_arcs_between_subsets - number of arcs between any subset of nodes
model.n = Param(within=NonNegativeIntegers)
model.max_out = Param(within=NonNegativeIntegers)
model.max_in = Param(within=NonNegativeIntegers)
model.arc_to_self = Param(within=NonNegativeIntegers)
model.min_arcs_between_subsets = Param(within=NonNegativeIntegers)

# create index sets:
# i = 1,..., n
# j = 1,..., n
# i,j for each i and j combination
model.I = RangeSet(1, model.n)
model.J = RangeSet(1, model.n)
model.IJ = model.I * model.J

# create distance parameter for each i and j combination
model.d = Param(model.I, model.J)

# declare a variable indexed by the set IJ
model.x = Var(model.IJ, domain=NonNegativeReals)

# declare objective function Dij * Xij
def obj_expression(model):
    return summation(model.d, model.x)

# declare objective variable
model.OBJ = Objective(rule=obj_expression)

# declare constraint: one and only one arc out of each node
def xi_constraint_rule(model, i):
    # return the expression for the constraint for i
    return sum(model.x[i,j] for j in model.J) >= model.max_out

# declare constraint: one and only one arc in each node
def xj_constraint_rule(model, j):
    # return the expression for the constraint for j
    return sum(model.x[i,j] for i in model.I) >= model.max_in

# declare constraint: no arcs to self
def arc_to_self_constraint_rule(model, i):
    # return the expression for the constraint for i
    return model.x[i,i] == model.arc_to_self

# create one constraint for each member of the set model.I
model.xiConstraint = Constraint(model.I, rule=xi_constraint_rule)

# create one constraint for each member of the set model.J
model.xjConstraint = Constraint(model.J, rule=xj_constraint_rule)

# create one constraint for each member of the set model.I
model.arcToSelfConstraint = Constraint(model.I, rule=arc_to_self_constraint_rule)
