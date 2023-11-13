# 판다스(pandas): 엑셀, csv, 2차원 데이터를 전처리 및 분석
#  - 수학 -> 0차원(스칼라), 1차원(벡터), 2차원(행렬), 3차원(텐서)
#  - 판다스 1차원(시리즈)
#  - 판다스 2차원(데이터프레임)
#  - 데이터프레임 -> df(약어)
#  - 엑셀(2차원), csv(2차원) -> 데이터 가져오기(데이터프레임)


import pandas as pd
import numpy as np

# 시리즈 생성
a = pd.Series([1, 2, 3], index=["a", "b", "c"])
print(a)

# 데이터프레임 생성
# 2차원 넘파이 배열(3, 3) 생성
arr1 = np.array([["광주여대", "3학년", "22"],
                 ["광주여대", "1학년", "20"],
                 ["광주여대", "2학년", "21"]])

# 열(column) 이름
col_names = ["학교", "학년", "나이"]

# 데이터프레임 생성하기
df_kwu = pd.DataFrame(arr1, columns=col_names)
print(df_kwu)

# 데이터프레임을 csv파일로 저장
#  - csv(,를 구분자로 하는 데이터 저장 방법)
#  - ex) "광주여대", "3학년", "22"
df_kwu.to_csv("./file.csv",
              header=True,
              index=False,
              encoding="UTF-8")

# csv 파일 불러와서 데이터프레임으로 사용하기!
df = pd.read_csv("./file.csv", sep=",")
print(df)

print("=" * 50)
print(df.columns)  # 제목열(특징) 가져오기

# 가정: 데이터 엄청 많음 -> 데이터가 올바르게 가져왔는지 확인
# head(), tail() -> 전체 데이터 중 5건만 가져와서 보여줌
print(df.head())  # -> 앞에서 부터 5건
print(df.tail())  # -> 뒤에서 부터 5건

# 탐색적 데이터 분석
# info()
#  1.데이터 n수, 특징(컬럼) 수
#  2.특징(컬럼) 데이터 타입 확인(int:정수, float:실수, object:문자열)
#  3.결측치 확인 (non-null: 값이 있음, null: 결측치)
#    - 결측치: 값이 누락(빈 칸)
print(df.info())

# 숫자 데이터만 출력!(빈도수, 평균, 표준편차, 최소값, 최대값 등)
print(df.describe())



