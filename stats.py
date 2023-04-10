import pandas as pd
import numpy as np

df1 = pd.read_csv('/Users/trung/Python Projects/Py-BasicStats/dataOne.csv')
df2 = pd.read_csv('/Users/trung/Python Projects/Py-BasicStats/dataTwo.csv')
df3 = pd.read_csv('/Users/trung/Python Projects/Py-BasicStats/dataThree.csv')
df0 = pd.read_csv('/Users/trung/Python Projects/Py-BasicStats/dataZero.csv')


#
# print(df1)
# print(df2)
# print(df3)
# print(df0)

def print_stats(x, y):
    print('Statistics Info:')
    print(f'Count X: {x.count()}')
    print(f'Count Y: {y.count()}')
    print(f'Mean X: {x.mean()}')
    print(f'Variance X: {x.var()}')
    print(f'Mean Y: {y.mean()}')
    print(f'Variance Y: {y.var()}')
    print(f'Correlation X and Y: {x.corr(y)}\n')


print_stats(df1['x'], df1['y'])
print_stats(df2['x'], df2['y'])
print_stats(df3['x'], df3['y'])
print_stats(df0['x'], df0['y'])

print("what do the statistics show you about these four data sets?")

#
# Write a couple of unit tests to test your various functions within the package.
