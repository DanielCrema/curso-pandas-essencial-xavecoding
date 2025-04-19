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