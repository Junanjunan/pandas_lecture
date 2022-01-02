""" 순위(Ranking) """

import pandas as pd
import numpy as np

s= pd.Series([-2, 4, 7, 3, 0, 7, 5, -4, 2, 6])

print(s)

print(s.rank())

print(s.rank(method='first'))       # 위에는 first 안해줬는데, 동일한 값이 .5로 나타남 / first를 해주면 먼저 오는 값에 rank를 우선순위를 줌
print(s.rank(method='max'))