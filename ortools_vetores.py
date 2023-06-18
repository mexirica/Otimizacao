import ortools.linear_solver.pywraplp as oplt
import pandas as pd
import numpy as np

#entrada
dados_geracao = pd.read_excel("inputs_dados.xlsx", sheet_name="geracao")
dados_carga = pd.read_excel("inputs_dados.xlsx", sheet_name="carga")
dados_dependencia = pd.read_excel("inputs_dados.xlsx", sheet_name="dependencia")
Ng = len(dados_geracao)

solver = oplt.Solver.CreateSolver('glop')

#entrada
Pg = np.zeros([Ng]).tolist()
for g in range(Ng):
    Pg[g] = solver.NumVar(0,float(dados_geracao.maximo[g]), f'Pg[{g}]')

#restrições
solver.Add(sum([Pg[g] for g in range(Ng)])==sum(dados_carga.valor))
for c in dados_dependencia.carga.unique():
    solver.Add(float(dados_carga.valor[c]) <= sum([Pg[g] for g in dados_dependencia.gerador[dados_dependencia.carga==c]]))

#obj
solver.Minimize(sum([Pg[g]*float(dados_geracao.custo[g]) for g in range(Ng)]))


results = solver.Solve()

if results == oplt.Solver.OPTIMAL:
    print('Resultado encontrado')
else:
    print("Resultado não encontrado")

for g in range(Ng):
    print('Pg[%i] = %.2f' % (g,Pg[g].solution_value()))