import pandas as pd

ufo = pd.read_csv('ufo.csv')

### loc ###

### loc if for selecting by labes / loc[[list of rows][list of columns]] - : is all

print(ufo.loc[0, :])
print()
print(ufo.loc[[0, 1, 2], :]) ### the same: ufo.loc.[0:2, :] loc is inclusive on both sides
print()
print(ufo.loc[0:3, 'City']) ### 'City':'State' - from : to /// [list] /// 'City', 'State', Others'
### The same as ufo.head(3).drop('Time', axis=1)

print(ufo[ufo.City == 'Oakland'])

print(ufo.loc[ufo.City == 'Oakland', 'State'])

### iloc ###

### iloc is exclusive on right side and inclusive on left side (only by integers)

print(ufo.iloc[:, 0:4])

print(ufo.iloc[0:3, :])

### ix ###

### alows mix loc and iloc

drinks = pd.read_csv('drinks.csv', index_col='country')

print(drinks.ix['Albania', 0])

print(drinks.ix['Albania':'Andorra', 0:2])