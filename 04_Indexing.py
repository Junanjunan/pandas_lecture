"""인덱싱 Indexing"""

import pandas as pd
import numpy as np

s = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd', 'e'])

print(s.keys())

print(s.items())    # zip으로 묶여서 나타난다
print(list(s.items()))  # 읽어주려면 list로 감싸준다

s['f'] = 1.25   # 새로운 값 추가

print(s)

print(s['a':'d'])
print(s[0:4])


print(s[(s > 0.4) & (s < 0.8)])     # filtering

print(s[['a', 'c', 'e']])       # 원하는 부분만


"""Series 인덱싱"""

s = pd.Series(['a', 'b', 'c', 'd', 'e'], index=[1, 3, 5, 7, 9])

print(s)

print(s.iloc[1])    # iloc은 정수값으로 index에 접근 첫 시작은 0부터 순서대로, 0,1,2,3...

print(s.iloc[2:4])


print(s.reindex(range(10)))    # reindex: index 재구성

print(s.reindex(range(10), method='bfill'))     # reindex할때, 전에 있는 값들로 구성


""" Dataframe 인덱싱 """

"""
df[val] : 하나의 컬럼 또는 여러 컬럼을 선택
df.loc[val] : 라벨값으로 로우의 부분집합 선택
df.loc[:, val] : 라벨값으로 컬럼의 부분집합 선택
df.iloc[where] : 정수 색인으로 로우의 부분집합 선택
df.iloc[:, where] : 정수 색인으로 컬럼의 부분집합 선택
df.iloc[where_i, where_j] : 정수 색인으로 로우와 컬럼의 부분집합 선택
df.at[label_i, label_j] : 로우와 컬럼의 라벨로 단일 값 선택
df.iat[i, j] : 로우와 컬럼의 정수 색인으로 단일 값 선택
reindex : 하나 이상의 축을 새로운 색인으로 재색인
get_value, set_value : 로우와 컬럼의 이름으로 값 선택
"""


pop_tuple = {'서울특별시': 123,
            '부산광역시': 456,
            '인천광역시':789
            }

population = pd.Series(pop_tuple)

male_tuple = {'서울특별시': 1,
        '부산광역시': 2,
        '인천광역시':3
        }

male = pd.Series(male_tuple)

female_tuple = {'서울특별시': 4,
        '부산광역시': 5,
        '인천광역시':6
            }

female = pd.Series(female_tuple)


korea_df = pd.DataFrame(
    {'인구수': population,
    '남자인구수': male,
    '여자인구수': female
    }
)


print(korea_df['남자인구수'])
print(korea_df.남자인구수)


korea_df['남여비율'] = (korea_df['남자인구수']*100/korea_df['여자인구수'])

print(korea_df.남여비율)

print(korea_df.values)  # 값들만

print(korea_df.T)       # 행과 열 바꾸기

print(korea_df.values[0])    # 한 줄만

print(korea_df['인구수'])

print(korea_df.loc[:'부산광역시', :'남자인구수'])

print(korea_df.loc[(korea_df.여자인구수 > 5)])

print(korea_df.loc[(korea_df.인구수 < 200)])

print(korea_df.loc[(korea_df.인구수 >100) & (korea_df.남여비율 < 50)])

print(korea_df.iloc[:3, :2])


"""
다중 인덱싱(Multi Indexing)
    - 1차원의 Series와 2차원의 DataFrame 객체를 넘어 3차원, 4차원 이상의 고차원 데이터 처리
    - 단일 인덱스 내에 여러 인덱스를 포함하는 다중 인덱싱
"""

idx_tuples = [('서울특별시', 2010), ('서울특별시', 2020),
                ('부산광역시', 2010), ('부산광역시', 2020),
                ('인천광역시', 2010), ('서울특별시', 2020),
]

print(idx_tuples)

pop_tuples = [123, 456,
                789, 101112,
                131415, 161718
]

population = pd.Series(pop_tuples, index=idx_tuples)

print(population)

midx = pd.MultiIndex.from_tuples(idx_tuples)
print(midx)

population = population.reindex(midx)

print(population)

print(population[:, 2010])

print(population['인천광역시', :])

# print(population.unstack()) ValueError: Index contains duplicate entries, cannot reshape
print("------")
print(korea_df.stack())
print("------")
print(korea_df.unstack())


male_tuples = [1,2,
            3,4,
            5,6,
            ]

korea_mdf = pd.DataFrame(
    {
        '총인구수': population,
        '남자인구수': male_tuples
    }
)

print(korea_mdf)

female_tuples = [
    6,5,
    4,3,
    2,1
]

korea_mdf = pd.DataFrame(
    {
        '총인구수': population,
        '남자인구수': male_tuples,
        '여자인구수': female_tuples
    }
)

print(korea_mdf)
print(korea_mdf.stack())

ratio = korea_mdf['남자인구수']*100/korea_mdf['여자인구수']
print(ratio)

# print(ratio.unstack())        # 오류 발생
# print(ratio.stack())          # 오류 발생

korea_mdf = pd.DataFrame(
    {
        '총인구수': population,
        '남자인구수': male_tuples,
        '여자인구수': female_tuples,
        '남여비율': ratio
    }
)

print(korea_mdf)


""" 다중 인덱스 생성 """

df = pd.DataFrame(
    np.random.rand(6, 3), 
    index=[['a', 'a', 'b', 'b', 'c', 'c'], [1,2,1,2,1,2,]], 
    columns=['c1', 'c2', 'c3']
    )

print(df)

pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b', 'c', 'c'], [1, 2, 1, 2, 1, 2]])
print(pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b', 'c', 'c'], [1, 2, 1, 2, 1, 2]]))

pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)])
print(pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]))

pd.MultiIndex.from_product([['a', 'b', 'c'], [1,2]])        # product : 곱하기
print(pd.MultiIndex.from_product([['a', 'b', 'c'], [1,2]]))

print(pd.MultiIndex(levels=[['a', 'b', 'c'], [1, 2]], codes=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]]))  # codes는 위치를 의미 - 0 첫번째, 1 두번째, 2 세번째

population.index.names = ['행정구역', '년도']       # index에 이름 붙이기

print(population)


idx = pd.MultiIndex.from_product(
    [['a', 'b', 'c'], [1, 2]],
    names=['name1', 'name2']
)

cols = pd.MultiIndex.from_product(
    [['c1', 'c2', 'c3',], [1, 2]],
    names = ['col_name1', 'col_name2']
)

data = np.round(np.random.randn(6, 6), 2)
mdf = pd.DataFrame(data, index=idx, columns = cols)
print(mdf)
print(mdf['c2'])


""" 인덱싱 및 슬라이싱 """

print(population['인천광역시', 2010])

print(population[:, 2010])

print(population[population > 300])

print(mdf['c2', 1])
print(mdf.iloc[:3, :4])
print(mdf.loc[:, ('c2', 1)])

idx_slice = pd.IndexSlice
print(idx_slice)
print(mdf.loc[idx_slice[:, 2], idx_slice[:, 2]]) # slice를 해주고, 행에서도 2에 해당하는 부분만, 열에서도 2에 해당하는 부분만


""" 다중 인덱스 재정렬 """

# print(korea_mdf['서울특별시':'인천광역시']) # pandas.errors.UnsortedIndexError: 'Key length (1) was greater than MultiIndex lexsort depth (0)' - 정렬을 해주어야 가능

korea_mdf = korea_mdf.sort_index()
print(korea_mdf)    # 가나다 순으로 정렬된 값이 출력된다
print(korea_mdf['서울특별시':'인천광역시']) # 정렬을 해주었기 때문에 이제 slicing이 가능하다고 함

# print(korea_mdf.unstack(level=0))   # 난 오류 발생
print(korea_mdf.stack(level=0))         # stack은 오류 안생김
korea_mdf.unstack()
print(korea_mdf.stack(level=1))       # IndexError: Too many levels: Index has only 1 level, not 2

# idx_flat = korea_mdf.reset_index(level=0) # ValueError: Index contains duplicate entries, cannot reshape
# print(idx_flat)