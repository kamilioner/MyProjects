import pandas as pd

### How to assign a user column names during a creation of a dataframe###

orders = pd.read_table('chipotle.tsv')
print(orders.head())

user_col = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_col)

print(users.head())