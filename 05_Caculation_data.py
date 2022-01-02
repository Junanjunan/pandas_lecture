""" 데이터 연산 """

import pandas as pd
import numpy as np

s = pd.Series(np.random.randint(0, 10, 5))

print(s)

df = pd.DataFrame(np.random.randint(0, 10, (3, 3)), columns=['A', 'B', 'C'])

print(df)

print(np.exp(s))

print(np.cos(df * np.pi / 4))

s1 = pd.Series([1, 3, 5, 7, 9], index = [0, 1, 2, 3, 4])
s2 = pd.Series([2, 4, 6, 8 , 10], index=[1, 2, 3, 4, 5])


print(s1 + s2) # index가 일치하지 않는 부분은 NaN 으로 표현됨

print(s1.add(s2, fill_value=0)) # fill_value: index가 일치하지 않아서 NaN으로 표현되는 부분에 값을 주는 것


df1 = pd.DataFrame(np.random.randint(0, 20, (3,3)), columns=list('ACD'))
print(df1)


df2 = pd.DataFrame(np.random.randint(0, 20, (5,5)), columns=list('BAECD'))
print(df2)

print(df1 + df2)    # 일치하지 않는 index가 많아서 그 부분들 다 NaN으로 표현됨

fvalue = df1.stack().mean()
print(fvalue)
print(df1.add(df2, fill_value = fvalue))


# add()

a = np.random.randint(1, 10, size=(3,3))
print(a)

print(a + a[0])

df = pd.DataFrame(a, columns=list('ABC'))
print(df)

print(df + df.iloc[0])
print(df.add(df.iloc[0]))

# sub() / subtract()
print(df - df.iloc[0])
print(df.sub(df.iloc[0]))
print(df.subtract(df.iloc[0]))
print(df.sub(df['B'], axis=0))      # axis : 2차원이니까 축을 지정할수 있다 함
print(df.subtract(df['B']))

# mul() / multiply()
print(df * df.iloc[1])
print(df.mul(df.iloc[2]))

# 나누기 : truediv() / div() / divide() / floordiv()

print(a / a[0])
print(df.truediv(df.iloc[0]))
print(df.div(df.iloc[1]))

print(a // a[0])
print(df.floordiv(df.iloc[0]))

print(a % a[0])     # %: 나머지 연산
print(df.mod(df.iloc[0]))

print(a ** a[0])
print(df.pow(df.iloc[0]))

row = df.iloc[0, ::2]   # step을 2로 주어서 row를 만들어보자
print(row)
print(df - row)