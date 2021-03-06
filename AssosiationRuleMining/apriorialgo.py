import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
from apyori import apriori
rules = apriori(transactions, min_support = 0.003 ,min_confidence = 0.2 ,min_lift = 3 ,min_lenght = 2)

results = list(rules)
results_list = []
for i in range(0, len(results)):
    results_list.append([str(results[i][0]).replace('frozenset({',"").replace("})",""), str(results[i][1]),str(results[i][2][0][2]),str(results[i][2][0][3])])
df = pd.DataFrame(results_list, columns = ['Result', 'Support', 'Confidence', 'lift'])
df.to_csv('Result.csv', index=False)