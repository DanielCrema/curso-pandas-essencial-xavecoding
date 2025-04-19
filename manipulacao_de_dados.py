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