
import pandas as pd
import numpy as np

def create_df(cols, idx):
    data = {c: [str(c.lower()) + str(i) for i in idx] for c in cols}
    return pd.DataFrame(data, idx)

df1 = create_df('AB', [1, 2])
print(df1)

df2 = create_df('AB', [3, 4])
print(df2)

print(pd.concat([df1, df2]))
print(pd.concat([df2, df1]))

df3 = create_df('AB', [0, 1])
df4 = create_df('CD', [0, 1])
print(pd.concat([df3, df4]))


print(pd.concat([df1, df3]))
# print(pd.concat([df1, df3], verify_integrity=True)) 
# df1, df3는 index 값이 충돌하는 것이 있다. 위에처럼 그냥 concat하면 충돌하는 것이 그대로 출력
# verify_integrity=True 를 넣어주면, index 값 등이 충돌할 때 에러가 있음을 알려주는 것으로 설정 (아마 column이 충돌할 때도 되지 않을까 싶음)

# 충돌 무시하고 강제로 하기
print(pd.concat([df1, df3], ignore_index=True))

# 추가적으로 키 부여하면서 concat하기
print(pd.concat([df1, df3], keys=['X', 'Y']))


df5 = create_df('ABC', [1, 2])
df6 = create_df('BCD', [3, 4])
print(pd.concat([df5, df6]))

# 둘다 중복되는 것만 즉 B,C만 concat 하기 - inner
print(pd.concat([df5, df6], join='inner'))

# 축사용하기 axis
print(pd.concat([df3, df4]))
print(pd.concat([df3, df4], axis=1))