import pandas as pd
import numpy as np
from ortools.sat.python import cp_model

nos = pd.read_excel("rotas_input.xlsx", sheet_name="nos")
caminhos = pd.read_excel("rotas_input.xlsx", sheet_name="caminhos")
n_nos = len(nos)
n_caminhos = len(caminhos)

model = cp_model.CpModel()
x = np.zeros(n_caminhos).tolist()
for c in caminhos.index:
    x[c] = model.NewIntVar(0,1,f"x[{c}]")

#FO
model.Minimize(sum([x[c] * caminhos.distancia[c] for c in caminhos.index]))

#restrições
no_origem = int(nos.no[nos.desc=="origem"].iloc[0])
no_destino =int(nos.no[nos.desc=="destino"].iloc[0])

model.Add(sum([x[c] for c in caminhos.index[caminhos.no_de==no_origem]])==1)
model.Add(sum([x[c] for c in caminhos.index[caminhos.no_para==no_destino]])==1)

for no in nos.no[nos.desc=="meio"]:
    sum_entrada = sum([x[c] for c in caminhos.index[caminhos.no_para==no]])
    sum_saida = sum([x[c] for c in caminhos.index[caminhos.no_de==no]])
    model.Add(sum_saida<=1)
    model.Add(sum_entrada<=1)
    model.Add(sum_entrada==sum_saida)

#Resolver
solver = cp_model.CpSolver()
status = solver.Solve(model)

#Print

print(f"Status = {solver.StatusName(status)}")
print(f"FO = {solver.ObjectiveValue()}")

caminhos['ativado'] = 0
for c in caminhos.index:
    caminhos.ativado[c] = solver.Value(x[c])
print(caminhos)

print("Rota escolhida")
for c in caminhos.index[caminhos.ativado==1]:
    print(" X%i%i - %.2f" % (caminhos.no_de[c], caminhos.no_para[c], caminhos.distancia[c]))