import pandas as pd

### String operations on Series ###

orders = pd.read_table('chipotle.tsv')

print(orders.head())

print(orders[orders.item_name.str.contains('Chicken')])

# orders.choice_description.str.replace('[', '').str.replace[']', '']
orders.choice_description = orders.choice_description.str.replace('[\[\]]', '')

print(orders.head())

