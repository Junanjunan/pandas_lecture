""" merge """

import pandas as pd
import numpy as np

df1 = pd.DataFrame(
    {
        '학생': ['홍길동', '이순신', '임꺽정', '김유신'],
        '학과': ['경영학과', '교육학과', '컴퓨터학과', '통계학과']
        }
)

df2 = pd.DataFrame(
    {
        '학생': ['홍길동', '이순신', '임꺽정', '김유신'],
        '입학년도': [2012, 2016, 2019, 2020]
        }
)


df3 = pd.merge(df1, df2)
print(df3)


df4 = pd.DataFrame(
    {
        '학과': ['경영학과', '교육학과', '컴퓨터학과', '통계학과'],
        '학과장': ['황희', '장영실', '안창호', '정약용']
        }
)

print(pd.merge(df3, df4))

df5 = pd.DataFrame(
    {
    '학과': ['경영학과', '교육학과', '교육학과', '컴퓨터학과', '컴퓨터학과', '통계학과'],
    '과목': ['경영개론', '기초수학', '물리학', '프로그래밍', '운영체제', '확률론']
    }
)

print(df5)

print(pd.merge(df1, df5))       # 학생이 중복되는 상황이 생김

print(pd.merge(df1, df2, on='학생'))    # on : 기준 

df6 = pd.DataFrame(
    {
        '이름': ['홍길동', '이순신', '임꺽정', '김유신'],
        '성적': ['A', 'A+', 'B', 'A+']
    }
)

print(pd.merge(df1, df6, left_on="학생", right_on="이름"))
print(pd.merge(df1, df6, left_on="학생", right_on="이름").drop("이름", axis=1))

mdf1 = df1.set_index('학생')        # index가 기존에는 0, 1, 2, 3 인데 '학생'을 index로 바꿔줌
mdf2 = df2.set_index('학생')        # index가 기존에는 0, 1, 2, 3 인데 '학생'을 index로 바꿔줌

print(mdf1)
print(df1)
print(mdf2)

print(pd.merge(mdf1, mdf2, left_index=True, right_index=True))
print(mdf1.join(mdf2))  #위와 동일한 결과물

print(pd.merge(mdf1, df6, left_index=True, right_on ='이름'))


df7 = pd.DataFrame(
    {
        '이름': ['홍길동', '이순신', '임꺽정'],
        '주문음식': ['햄버거', '피자', '짜장면']
    }
)

df8 = pd.DataFrame(
    {
        '이름': ['홍길동', '이순신', '김유신'],
        '주문음료': ['콜라', '사이다', '커피']
    }
)

print(pd.merge(df7, df8))  # 위에서 겹치는 부분만 merge가 됨을 볼 수있다(홍길동, 이순신)
print(pd.merge(df7, df8, how='inner')) # 위에것과 동일 - inner는 default임
print(pd.merge(df7, df8, how='outer')) # 모두 포함
print(pd.merge(df7, df8, how='left'))   # 왼쪽 것 기준 - 여기선 df7
print(pd.merge(df7, df8, how='right'))  # 오른쪽 것 기준 - 여기선 df8

df9 = pd.DataFrame(
    {
        '이름': ['홍길동', '이순신', '임꺽정', '김유신'],
        '순위': [3, 2, 4, 1]
    }
)

df10 = pd.DataFrame(
    {
        '이름': ['홍길동', '이순신', '임꺽정', '김유신'],
        '순위': [4, 1, 3, 2]
    }
)

print(pd.merge(df9, df10, on='이름'))   # 순위가 겹치는데 뒤에 _ 붙여서 자동생성
print(pd.merge(df9, df10, on='이름', suffixes=["_인기", "_성적"]))  # 겹치는 것에 이름 부여
