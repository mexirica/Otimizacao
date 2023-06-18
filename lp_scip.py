import ortools.linear_solver.pywraplp as otlp

solver = otlp.Solver.CreateSolver('glop')

x = solver.NumVar(-solver.infinity(),3,"x")
y = solver.NumVar(0,solver.infinity(),"y")

solver.Add(x+y<=8)
solver.Add(8*x+3*y>=-24)
solver.Add(-6*x+8*y<=48)
solver.Add(3*x+5*y<=15)

solver.Minimize(-4*x-2*y)

results = solver.Solve()

if results == otlp.Solver.OPTIMAL:
    print("Resultado encontrado")
else:
    print("Resultando não encontrado")

print('x=', x.solution_value())
print('y=', y.solution_value())