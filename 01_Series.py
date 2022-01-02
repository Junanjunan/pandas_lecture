import pandas as pd

""" Series """

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0])

print(s.values)

print(s.index)

print(s[1])

print(s[1:4])

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd', 'e'])

print(s)

print(s['c'])

print(s[['c', 'd', 'e']])

print('b' in s)

s = pd.Series([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

print(s)
print(s.unique())   # unique한 값만 뽑아준다

print(s.value_counts())  # value 갯수 알려준다

print(s.isin([2, 4]))   # 해당하는 값이 어디에 속해있는지 bool 값으로 표시

pop_tuple = {'서울특별시': 123,
            '부산광역시': 456,
            '인천광역시':789
            }

population = pd.Series(pop_tuple)

print(population)

print(population['서울특별시'])
print(population['서울특별시':'인천광역시'])




