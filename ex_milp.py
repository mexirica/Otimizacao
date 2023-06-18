import ortools.linear_solver.pywraplp as otlp
import numpy as np

solver = otlp.Solver.CreateSolver('cbc')

x = [solver.IntVar(0,solver.infinity(), f'x{i}') for i in range(6)]
y = solver.NumVar(0,solver.infinity(),"y")

solver.Add(sum([x[i] for i in range(1,6)])+y<=20)

for i in range(1,6):
    solver.Add(x[i]+y>=15)

solver.Add(sum([i * x[i] for i in range(1,6)])>=10)

solver.Add(x[5]+2*y>=30)

solver.Minimize(sum([x[i] for i in range(1,6)])+y)

results= solver.Solve()

if results == otlp.Solver.OPTIMAL:
    print("Resultado encontrado")
else:
    print("Resultado não encontrado")

for i in range(1,6):
    print(f'x[{i}] = {x[i].solution_value()}')
print(f'y = {round(y.solution_value(), 2)}')
