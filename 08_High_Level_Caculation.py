""" 고성능연산 """

import pandas as pd
import numpy as np

nrows, ncols = 100000, 100
df1, df2, df3, df4 = (pd.DataFrame(np.random.rand(nrows, ncols)) for i in range(4))

print(df1 + df2 + df3 +df4)
print(pd.eval('df1 + df2 + df3 + df4'))
# 위의 두 식은 결과는 같은데 pandas를 이용한 것이 속도가 더 빠른것으로 나온다. 아래 식도 마찬가지
# 강의에서는 %timeit pd.eval('df1 + df2 + df3 + df4') 라는 것을 이용하는데 VSC에서는 없는 듯...

print(df1 * df2 / (-df3 * df4))
print(pd.eval('df1 * df2 / (-df3 * df4)'))

# 아래와 같이 산식이 많아 질수록 시간차가 커진다

print((df1 < df2) & (df2 <= df3) & (df3 != df4))
print(pd.eval('(df1 < df2) & (df2 <= df3) & (df3 != df4)'))

# 계산 시간이 오래걸리는 것들은 pandas의 eval 연산자를 사용하면 빨리 되니 이용하자

df = pd.DataFrame(np.random.rand(1000000, 5), columns=['A', 'B', 'C', 'D', 'E'])
print(df.head())

print(df['A'] + df['B'] / df['C'] - df['D'] * df['E'])
print(pd.eval("df['A'] + df['B'] / df['C'] - df['D'] * df['E']"))

# column 명으로 바로 접근도 가능

print(df.eval('A + B / C - D * E'))

# 계산을 해서 바로 반영도 가능
print(df.eval('R = A + B / C - D * E', inplace=True)) # (R column이 추가됨)
print(df.head())
