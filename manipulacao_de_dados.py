import pandas as pd

# Loading dataset
dataset = pd.read_csv('datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

# Printing dataset
print(dataset.head())
print(dataset.tail())