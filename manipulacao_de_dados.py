import pandas as pd

# Loading dataset
dataset = pd.read_csv('datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

# Printing dataset
print(dataset.head())
print(dataset.tail())

# Printing info about the dataset
print(dataset.info())

# Check dataframe type
type(dataset)

# Check dataframe shape
dataset.shape
print(f'The dataframe has {dataset.shape[0]} rows/observations/registers and {dataset.shape[1]} columns/attributes/variables.')

# Creating a dataframe from a dictionary
characters_df = pd.DataFrame({
    'name': ['Luke Skywalker', 'Yoda', 'Palpatine'],
    'age': [16, 1000, 70],
    'weight': [70.5, 15.2, 60.1],
    'is_jedi': [True, True, False]
})
print(characters_df)
characters_df.info()

# Dataframe methods
characters_df.columns
type(characters_df.columns)
list(characters_df.columns)

# Rename columns
renamed_characters_df = characters_df.rename(columns={
    'name': 'character_name',
    'age': 'character_age'
    })
print(renamed_characters_df)

# Rename inplace
characters_df.rename(columns={
    'name': 'character_name',
    'age': 'character_age'
    }, inplace=True)

# Other way of renaming
characters_df.columns = ['character_name', 'character_age', 'character_weight', 'is_jedi']

# Series
# Series is a one-dimensional array-like object containing data and labels of columns or rows
# 
# Selecting a whole column
dataset['ESTADO']
dataset.ESTADO
type(dataset['ESTADO'])

# Selecting info by index
dataset.iloc[0]
type(dataset.iloc[0])

# Creating a Series
pd.Series([5.5, 6.0, 9.5])

# Changing name of indexes in a Series
pd.Series([5.5, 6.0, 9.5], index=['exam1', 'exam2', 'project'], name='Luke Skywalker scores')

# Attributing Data
# 
# Attributing constants
product_view = dataset['PRODUTO']
product_view.head()

# Attributing a constant to all rows
dataset_copy_bkp = dataset.copy()
dataset['PRODUTO'] = 'Combustível'
dataset['PRODUTO'].head()

# Attributing lists or series
dataset.shape
new_products = [f'Produto {i}' for i in range(dataset.shape[0])]
dataset['PRODUTO'] = new_products
dataset['PRODUTO']

# Recovering from backup
dataset['PRODUTO'] = dataset_copy_bkp['PRODUTO']
dataset['PRODUTO']

# Creating new columns
# 
# From constant
dataset['crazy column'] = 'DEFAULT'
dataset['crazy column']

# From a list
dataset['crazy column from list'] = range(dataset.shape[0])
dataset['crazy column from list']
dataset['lenght error'] = range(dataset.shape[0] + 1) # Returns an error

# Creating a column from an existing one
dataset['PREÇO MÉDIO REVENDA (dólares)'] = dataset['PREÇO MÉDIO REVENDA'] * 6.0
dataset['PREÇO MÉDIO REVENDA (dólares)']

# Indexes
# 
dataset.index

# Example of Dataframe with textual indexes (labels)
satisfaction_research = pd.DataFrame({
    'good': [10, 20, 30],
    'bad': [10, 20, 30],
    'neutral': [10, 20, 30]
}, index=['xboxOne', 'Playstation5', 'NintendoSwitch'])
satisfaction_research.head()

# Selecting one or more samples (indexing)
# 
# Index based selection
dataset.iloc[1] # Selects index 1
dataset.iloc[:6] # Selects first 5 indexes
dataset.iloc[10:16] # Selects indexes from 10 to 15
dataset.iloc[[1, 5, 10, 15]] # Selects indexes 1, 5, 10 and 15
dataset.iloc[[5, 1, 15, 10]] # Selects the same, but out of order
dataset.iloc[1][4] # Selects index 1 and column 4

# Label based selection
satisfaction_research.loc['xboxOne'] # Returns the row with label 'xboxOne'
satisfaction_research.loc['Playstation5']['bad'] # Returns the value of the 'bad' column in the row with label 'Playstation5'
satisfaction_research.loc[['xboxOne', 'NintendoSwitch']] # Returns the rows with labels 'XboxOne' and 'NintendoSwitch'
satisfaction_research[['good', 'bad']] # Returns the columns with labels 'good' and 'bad'
satisfaction_research.loc[:, ['good', 'bad']] # Same using loc

# Selecting one or more attributes (columns)
# 
dataset.head()

# Selecting one column
dataset['ESTADO']
dataset.ESTADO # Only works when column name has no invalid characters (spaces, special characters, etc.)
dataset.loc[:, 'ESTADO']

# Selecting multiple columns
dataset[['PRODUTO', 'ESTADO', 'REGIÃO']]

# Conditional Selection: Filtering samples
# 
dataset['ESTADO'].unique() # Shows unique values for the attribute 'ESTADO'
dataset['ESTADO'].value_counts() # Shows the number of occurrences of each unique value for the attribute 'ESTADO'
dataset['ESTADO'] == 'SAO PAULO' # Returns a Series with booleans True or False for each sample
selection = dataset['ESTADO'] == 'SAO PAULO' # Stores the result of the previous operation in a variable
selection.shape
dataset[selection] # Returns the samples that have 'ESTADO' equal to 'SAO PAULO'
dataset.loc[selection] # Same as above using loc

# Using the .query() method
# 
gas_stations_sp = dataset.query('ESTADO == "SAO PAULO"') # Returns the samples that have 'ESTADO' equal to 'SAO PAULO'
gas_stations_sp.head()
gas_stations_sp.shape

# Resetting indexes
gas_stations_sp.reset_index() # Returns the dataframe with the index reset and a new column 'index' with the original indexes at column [0]
gas_stations_sp.reset_index(drop=True) # Drop index column
gas_stations_sp.reset_index(drop=True, inplace=True) # Drop index column and update dataframe inplace
gas_stations_sp = dataset.query('ESTADO == "SAO PAULO"').reset_index(drop=True) # Reset index and drop index column in one line
dataset.query('ESTADO == "SAO PAULO" or ESTADO == "RIO DE JANEIRO"') # Returns the samples that have 'ESTADO' equal to 'SAO PAULO' or 'RIO DE JANEIRO'
gas_stations_sp.head()

# Conditional Selection with multiple conditions
# 
dataset['ESTADO'].unique()
dataset['ESTADO'] == 'RIO DE JANEIRO' # Returns a Series with booleans True or False for each sample
dataset['PREÇO MÉDIO REVENDA'] > 2.0 # Returns a Series with booleans True or False for each sample
selection = (dataset['ESTADO'] == 'RIO DE JANEIRO') & (dataset['PREÇO MÉDIO REVENDA'] > 2) # Returns a Series with booleans True or False for each sample
(dataset['ESTADO'] == 'RIO DE JANEIRO') & (dataset['PREÇO MÉDIO REVENDA'] > 2) # Returns a Series with booleans True or False for each sample
(dataset['ESTADO'] == 'RIO DE JANEIRO') | ~ (dataset['PREÇO MÉDIO REVENDA'] > 2) # Returns a Series with booleans True or False for each sample
dataset['ESTADO']
dataset['PREÇO MÉDIO REVENDA']
dataset['ESTADO' == 'RIO DE JANEIRO' & dataset['PREÇO MÉDIO REVENDA' > 2]]
dataset[selection].reset_index(drop=True) # Returns the samples that have 'ESTADO' equal to 'RIO DE JANEIRO' and 'PREÇO MÉDIO REVENDA' greater than 2

# Going deeper
selection_1 = dataset['ESTADO'] == 'RIO DE JANEIRO'
gas_stations_rj = dataset[selection_1]
selection_2 = gas_stations_rj['PREÇO MÉDIO REVENDA'] > 2
gas_stations_rj_minimun_price_greater_than_2 = gas_stations_rj[selection_2]
gas_stations_rj_minimun_price_greater_than_2.reset_index(drop=True)

# Selecting samples of stations from SP and RJ with Common Gas above R$2.00
# 
# Slow inneficient way
dataset.shape
dataset.head()
selection_1 = (dataset['ESTADO'] == 'SAO PAULO') | (dataset['ESTADO'] == 'RIO DE JANEIRO')
selection_1
selection_2 = dataset['PRODUTO'] == 'GASOLINA COMUM'
selection_2
selection_3 = dataset['PREÇO MÉDIO REVENDA'] > 2.0
selection_3
final_selection = selection_1 & selection_2 & selection_3
final_selection
# Filtering
filtered_dataset = dataset[final_selection]
print(filtered_dataset['ESTADO'].unique())
print(filtered_dataset['PRODUTO'].unique())

# Fast and efficient way
dataset['ESTADO'].value_counts() # SP and RJ both feature 4263 gas stations (sums up to 8526)
dataset['PRODUTO'].value_counts() # GASOLINA COMUM counts 21194
# 
# Most efficient way is to filter ESTADO first
selection_1 = (dataset['ESTADO'] == 'SAO PAULO') | (dataset['ESTADO'] == 'RIO DE JANEIRO') # 8526
selection_1 = dataset['ESTADO'].isin(['SAO PAULO', 'RIO DE JANEIRO']) # Same as above
gas_stations_sp_rj = dataset[selection_1] # 8526
selection_2 = (gas_stations_sp_rj['PRODUTO'] == 'GASOLINA COMUM') # 21194
selection_2
gas_stations_sp_rj['PRODUTO'].value_counts() # GASOLINA COMUM == 1570
gas_stations_sp_rj_gasoline = gas_stations_sp_rj[selection_2] # 1570
gas_stations_sp_rj_gasoline
(gas_stations_sp_rj_gasoline['PREÇO MÉDIO REVENDA'] > 2.0).value_counts() # True = 1564
selection_3 = gas_stations_sp_rj_gasoline['PREÇO MÉDIO REVENDA'] > 2.0
gas_stations_sp_rj_gasoline_prices_greater_than_2 = gas_stations_sp_rj_gasoline[selection_3]
gas_stations_sp_rj_gasoline_prices_greater_than_2

# Selecting samples from years 2008, 2010 and 2012
# 
# Alternative 1
selection = (dataset['ANO'] == 2008) | (dataset['ANO'] == 2010) | (dataset['ANO'] == 2012)
dataset[selection]['ANO'].unique()
dataset[selection]

# Alternative 2
years_list =  [2008, 2010, 2012]
selection = dataset['ANO'].isin(years_list) # Returns a Series with booleans True or False for each sample
dataset[selection]

# Alternative 3
dataset.query('ANO in @years_list')

# Iterating with DataFrames
# => Inneficient method
for index, row in dataset.head(10).iterrows(): # Iterates over the first 10 rows of the dataset
    print(f'Index {index} -> {row['ESTADO']}')


# Data cleaning
#
 
# Preparation of data
# 
dataset.info()
dataset_pre = dataset.copy()

# Converting types of attributes
# 
# Converting dates
dataset_pre['DATA INICIAL']
dataset_pre['DATA FINAL']
dataset_pre['DATA INICIAL'] = pd.to_datetime(dataset_pre['DATA INICIAL'])
dataset_pre['DATA FINAL'] = pd.to_datetime(dataset_pre['DATA FINAL'])
dataset_pre.info()

# Converting string attributes to numbers
for attribute in ['MARGEM MÉDIA REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO', 'DESVIO PADRÃO DISTRIBUIÇÃO', 'PREÇO MÍNIMO DISTRIBUIÇÃO', 'PREÇO MÁXIMO DISTRIBUIÇÃO', 'COEF DE VARIAÇÃO DISTRIBUIÇÃO']:
    # Converts to float, in case of error, converts to NaN
    dataset_pre[attribute] = pd.to_numeric(dataset_pre[attribute], errors='coerce')
dataset_pre.info()

# Treating observations with empty values (null/NaN) in the dataset_pre
mask = dataset_pre['PREÇO MÉDIO DISTRIBUIÇÃO'].isnull()
mask
dataset_pre[mask]['PREÇO MÉDIO DISTRIBUIÇÃO']
dataset[mask]['PREÇO MÉDIO DISTRIBUIÇÃO'] # Check the original values
dataset.info() # Returns NO null-values, but in fact, there are

# Cases of treatment
# 
# Fill NaN with 0
dataset_pre_fill = dataset_pre.copy()
dataset_pre_fill = dataset_pre['PREÇO MÉDIO DISTRIBUIÇÃO'].fillna(0)
dataset_pre_fill[mask]

# Fill NaN with a constant values
dataset_pre_fill = dataset_pre.fillna(value={
    'PREÇO MÉDIO DISTRIBUIÇÃO': 10,
    'DESVIO PADRÃO DISTRIBUIÇÃO': 20,
    'PREÇO MÍNIMO DISTRIBUIÇÃO': 30,
    'PREÇO MÁXIMO DISTRIBUIÇÃO': 'vazio'
})
dataset_pre_fill[mask][[ 'PREÇO MÉDIO DISTRIBUIÇÃO', 'DESVIO PADRÃO DISTRIBUIÇÃO', 'PREÇO MÍNIMO DISTRIBUIÇÃO', 'PREÇO MÁXIMO DISTRIBUIÇÃO']]

# Remove samples with NaN
dataset_pre_drop = dataset_pre.dropna()
dataset_pre_drop.info()
# Remove inplace
dataset_pre.dropna(inplace=True)
dataset_pre.info()
dataset_pre.to_csv('./datasets/GasPricesinBrazil_2004-2019_preprocessed.csv', index=False)