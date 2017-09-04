import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

train = pd.read_csv('titanic_train.csv')

print((train.head()))

train['Sex_num'] = train.Sex.map({'female': 0, 'male': 1})
print(train.loc[0:4, ['Sex', 'Sex_num']])

train['Name_length'] = train.Name.apply(len)
print(train.loc[0:4, ['Name', 'Name_length']])

train['Fare_ceil'] = train.Fare.apply(np.ceil)
print(train.loc[0:4, ['Fare', 'Fare_ceil']])


def get_element(my_list, position):
    return my_list[position]


train['Name_shortened'] = train.Name.str.split(',').apply(get_element, position=0)
# train['Name_shortened'] = train.Name.str.split(',').apply(lambda x: x[0])
print(train.loc[0:4, ['Name', 'Name_shortened']])

drinks = pd.read_csv('drinks.csv')

print(drinks.loc[:, 'beer_servings': 'wine_servings'].apply(max, axis=0))
print(drinks.loc[:, 'beer_servings': 'wine_servings'].apply(np.argmax, axis=1))

print(drinks.loc[:, 'beer_servings': 'wine_servings'].applymap(float))
drinks.loc[:, 'beer_servings': 'wine_servings'] = drinks.loc[:,
                                                             'beer_servings': 'wine_servings'].applymap(float)
print(drinks.head())
