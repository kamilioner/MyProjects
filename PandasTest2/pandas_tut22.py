import pandas as pd

train = pd.read_csv('http://bit.ly/kaggletrain')

print(train.head())

train['Sex_male'] = train.Sex.map({'female': 0, 'male': 1})

print(train.head())

print(pd.get_dummies(train.Sex, prefix='Sex').iloc[:, 1:])

train['Embarked'].value_counts()

embarked_dummies = pd.get_dummies(train['Embarked'], prefix='Embarked').iloc[:, 1:]

train = pd.concat([train, embarked_dummies], axis=1)

print(train.head())

### To drop and replce the 1/0 I got all the work upper to this line:

train = pd.read_csv('http://bit.ly/kaggletrain')

print(pd.get_dummies(train, columns=['Sex', 'Embarked'], drop_first=True).head())

