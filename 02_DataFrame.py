""" DataFrame 객체 """

import pandas as pd
import numpy as np

print(pd.DataFrame([{'A':2, 'B':4, 'D':3}, {'A':4, 'B':5, 'C':7}]))

print(pd.DataFrame(np.random.rand(5, 5)))

print(pd.DataFrame(np.random.rand(5, 5), columns=['A', 'B', 'C', 'D', 'E'], index=[1, 2, 3, 4, 5]))



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

print(korea_df)


print(korea_df.index)

print(korea_df.columns)

print(korea_df['여자인구수'])

print(korea_df['서울특별시':'부산광역시'])