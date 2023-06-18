#Ortools não resolve problemas não lineares

import ortools.linear_solver.pywraplp as otlp

solver = otlp.Solver.CreateSolver('glop')

x = solver.NumVar(0,solver.infinity(),"x")
y = solver.NumVar(0,solver.infinity(),"y")

solver.Add(2*x+y<=100)

solver.Maximize(x*y)

results=solver.Solve()

if results == otlp.Solver.OPTIMAL:
    print("Resultado encontrado")
else:
    print("Resultado não encontrado")

print(f'x = {x.solution_value()}')
print(f'y = {y.solution_value()}')

