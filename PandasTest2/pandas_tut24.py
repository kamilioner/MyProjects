import pandas as pd

user_col = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|',
                      header=None, names=user_col, index_col='user_id')

print(users.head())

print(users['zip_code'].duplicated())
print()
print(users['zip_code'].duplicated().sum())
print()
print(users.duplicated())
print(users.duplicated().sum())
# first dupicates // 'last' <- last duplicates // False <- all dupicates
print(users.loc[users.duplicated(keep='first'), :])

print(users.drop_duplicates(keep='first').shape)

print(users.duplicated(subset=['age', 'zip_code']).sum())
print(users.drop_duplicates(subset=['age', 'zip_code']).shape)
