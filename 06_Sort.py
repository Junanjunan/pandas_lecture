""" 정렬(Sort) """

import pandas as pd
import numpy as np

s = pd.Series(range(5), index=['A', 'D', 'B', 'C', 'E'])
print(s)

print(s.sort_index())   # 인덱스로 정렬 - 알파벳순
print(s.sort_values())  # 값으로 정렬 - 커지는 순

df = pd.DataFrame(
    np.random.randint(0, 10, (4, 4)),
    index = [2, 4, 1, 3],
    columns = list('BDAC')
)

print(df)

print(df.sort_index())
# print(df.sort_values()) # 이렇게만 하면 오류 생김, 기준이 필요 - by
print(df.sort_values(by='A'))   # A column은 value를 정렬(커지느 순) - 나머지 열들은 A를 기준으로 따라옴
print(df.sort_values(by=['A', 'C']))    # 두가지를 기준으로 정렬이 가능한데, 먼저 선언된 A가 우선순위임

print(df.sort_index(axis=1))    # 축 지정 가능 - 기본으로 하면 index 순으로 정렬, axis=1 로 하면 컬럼이 정렬되는 듯 (ABCD)