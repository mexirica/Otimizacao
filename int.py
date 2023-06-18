import ortools.linear_solver.pywraplp as otlp

solver = otlp.Solver.CreateSolver('cbc')

x = solver.IntVar(0, 10, "x")
y = solver.NumVar(0, 10, "y")

solver.Add(-x + 2 * y <= 7)
solver.Add(2 * x + y <= 14)
solver.Add(2 * x - y <= 10)

solver.Maximize(x + y)

results = solver.Solve()

if results == otlp.Solver.OPTIMAL:
    print("Resultado encontrado")
else:
    print("Resultado não encontrado")

# Resolve o problema antes de imprimir os valores das variáveis
solver.Solve()

print(f'x={x.solution_value()}')
print(f'y={y.solution_value()}')
