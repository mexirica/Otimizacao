import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import numpy as np

model = pyo.ConcreteModel()

model.N = pyo.Var(within=Integers, bounds=(0,None))
model.p = pyo.Var(bounds=(50,200))
p = model.p
N = model.N

model.obj = pyo.Objective(expr = p*N, sense=maximize)
model.C1 = pyo.Constraint(expr = N == 1001-5*p)

opt = SolverFactory('couenne', executable='C:\\couenne\\bin\\couenne.exe')
opt.solve(model)

print(f'p = {np.round(pyo.value(p))}')
print(f'N = {np.round(pyo.value(N))}')
print(f'Receita = {pyo.value(p)*pyo.value(N)}')