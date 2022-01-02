""" Index 객체 """

"""
클래스 종류 Index, Int64Index, MultiIndex, DatetimeIndex, PeriodIndex

Index: 일반적인 Index 객체이며, Numpy 배열 형식으로 축의 이름 표현
Int64Index : 정수값을 위한 Index
MultiIndex : 단일 축에 여러 단계 색인을 표현하는 계층적 Index 객체 (튜플의 배열과 유사)
DatetimeIndex : Numpy의 datetime64 타입으로 타임스탬프 저장
PeriodIndex : 기간데이터를 위한 Index
"""

import pandas as pd

idx = pd.Index(([2, 4, 6, 8, 10]))

print(idx)

print(idx[1])

print(idx[0:4:2])       # 맨 끝은 index가 증가량 의미

print(idx[-1::])        

print(idx[::2])         # step, 건너뛰기

print(idx.size)
print(idx.shape)
print(idx.ndim) # 차원수
print(idx.dtype)

"""
메소드
append: 색인 객체를 추가한 새로운 색인 반환
difference: 색인의 차집합 반환
intersection: 색인의 교집합 반환 - 연산자: &
union: 색인의 합칩합 반환 - 연산자 : |
isin: 색인이 존재하는지 여부를 불리언 배열로 반환
delete: 색인이 삭제된 새로운 색인 반환
drop: 값이 삭제된 새로운 색인 반환
insert: 색인이 추가된 새로운 색인 반환
is_monotonic: 색인이 단조성을 가지면 True
is_unique: 중복되는 색인이 없다면 True
unique: 색인에서 중복되는 요소를 제거하고 유일한 값만 반환
symmmetric_difference: 합집합 - 교집합
"""

idx1 = pd.Index([1,2,4,6,8])
idx2 = pd.Index([2,4,5,6,7])
print(idx1.append(idx2))
print(idx1.difference(idx2))
print(idx1 - idx2)
print(idx1.intersection(idx2))
# print(idx1 & idx2) - 연산자 사용시 나는 오류 발생
print(idx1.union(idx2))
# print(idx1 | idx2) - 연산자 사용시 나는 오류 발생
print(idx1.delete(0))   # 첫번째 값 삭제
print(idx1.drop(2))     # 값이 2인 것을 삭제
# print(idx1 ^ idx2) - 연산자 사용시 나는 오류 발생
print(idx1.symmetric_difference(idx2))  # idx1과 idx2에서 합집합에서 교집합을 뺀 부분