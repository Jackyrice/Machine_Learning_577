import sys
import gurobipy as gp
import pandas as pd
import numpy as np
from gurobipy import GRB
#first question
m1 = gp.read("salad_kp.mps")
m1.optimize()

#second question
data = pd.read_csv("new_fruits.csv")
m2 = m1.copy()
st = m2.getConstrByName('Knapsack')
m2.addVar(lb=0,ub=1,obj=18,name="pineapple",column=gp.Column([2], [st]))
m2.addVar(lb=0,ub=2,obj=1.5,name="Watermelon",column=gp.Column([4], [st]))
m2.update()
m2.optimize()

#Third question
new = np.load('new_fruit_values.npy')
c = new[1,:]
m3 = m2.copy()
x = m3.getVars()
nf = []
for i in range(6):
    nf += c[i]*x[i]
m3.setObjective(nf, GRB.MAXIMIZE)
m3.optimize()

#Report
print("Anwser1: %s" %m1.getVars())
print("Anwser2: %s" %m2.getVars())
print("Anwser3: %s" %m3.getVars())