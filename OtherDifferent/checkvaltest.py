import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

checkv = pd.read_csv('C:/Users/A660197/Desktop/checkval.csv', encoding="ISO-8859-1", low_memory=False)

# print(checkv.head())

checkv = checkv.loc[(checkv['CUST'] == 'CARMAX') & (checkv['DATA SOURCES'].str.contains('SNOW')) & (checkv['DATA SOURCES'].str.contains('SEVONE')),:]

print(str(len(checkv.index)) + 'x' + str(len(checkv.columns)))