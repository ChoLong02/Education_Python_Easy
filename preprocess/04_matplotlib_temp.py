# 기온 CSV 데이터 시각화

import matplotlib.pyplot as plt
import pandas as pd

# 상대경로
#   .. → 현재 폴더에서 뒤로가기     ↑
#   . → 현재 위치에서               -
#   / → 더블클릭(폴더 열기)         ↓

df = pd.read_csv("./dataset/기온.csv",
                 encoding="cp949")
# head(), tail() → 데이터 로드 확인용도
#  - () → default(5)
print(df.head(3))  # 위에서부터 3건만 출력

# 탐색적 데이터 분석
#  - 데이터: 365건
#  - 인덱스: 0~364
#  - column(특징): 8개(지점, 지점명, 일시, 평균기온, 최저기온, 최저기온 시각, 최고기온, 최고기온 시각)
#    Object(문자열), int(정수), float(실수)
#  - 결측치: 최저기온(1), 최저기온시각(1)
print(df.info())

# 결측치 처리
#  - 이전 행의 값으로 채우기(기온)
#  - 신장데이터, 점수(평균)
#  - fillna() : 결측치 채우기    na=null=결측치
#  - ffill : front fill

# ** 결측치 채우기
#  - 대표값: 평균, 중앙값, 최빈값
#  - 이전행, 다음행
#  - 회귀분석 → 예측값
df2 = df.fillna(method="ffill")
print(df2.info())

# 특수문자 포함 된 제목열 이름 변경
#  - rename() : 제목열 이름 변경
df2.rename(columns={"최저기온(°C)": "min_temp"}, inplace=True)
df2.rename(columns={"평균기온(°C)": "avg_temp"}, inplace=True)
df2.rename(columns={"최고기온(°C)": "max_temp"}, inplace=True)
print(df2.head(3))

plt.title("Seoul 2022 temp")
plt.plot(range(1, len(df2)+1), df2["max_temp"], label="max", c='r')
plt.plot(range(1, len(df2)+1), df2["avg_temp"], label="avg", c='y')
plt.plot(range(1, len(df2)+1), df2["min_temp"], label="min", c='b')
plt.xlabel("일")
plt.ylabel("기온")
plt.legend()
plt.show()