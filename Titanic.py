import pandas as pd

df = pd.read_csv('titanic.csv', index_col='PassengerId')

print(df.head(1))
print('')
# Заголовок
#print('Заголовок - ' + str(df.head(5)))
print('Количество мужчин и женщин:')
print(df['Sex'].value_counts())
print('')


print('Доля выживших:')
print(round(df['Survived'].value_counts()[1] / df.shape[0], 2))
print('')

print('Доля пассажиров 1 класса:')
print(round(df['Pclass'].value_counts()[1] / df.shape[0], 2))
print('')

print('Доля пассажиров 1 класса:')
print(round(df['Pclass'].value_counts()[1] / df.shape[0], 2))
print('')