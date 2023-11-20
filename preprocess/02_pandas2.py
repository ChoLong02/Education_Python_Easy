import pandas as pd

list1 = list([["허준호", "남자", 30, 183],
              ["이가원", "여자", 24, 162],
              ["배규민", "남자", 23, 179],
              ["고고림", "남자", 21, 182],
              ["이새봄", "여자", 28, 160],
              ["이보람", "여자", 26, 163],
              ["이루리", "여자", 24, 157],
              ["오다현", "여자", 24, 172]])
col_names = ["이름", "성별", "나이", "키"]
df = pd.DataFrame(list1, columns=col_names)
print(df)

# 조건 → 키가 180넘는 사람
#  - 특징 선택 df["특징명"]
#  - 조건: df["키"] >= 180
#  - 실행: df[조건]
print(df[df["키"] >= 180])

# 조건 2개인 경우!
#  조건1) 성별이 여자  (df["성별"] == "여자")
#  조건2) 키 >= 160   (df["키"] >= 160)

# 논리연산자
#   1. &(AND): 2개의 조건이 모두 참인 경우에만 참
#     - 성별이 여자이면서 키가 160cm 이상인 사람 추출
#   2. |(OR): 1개의 조건만 참이면 참
#     - 성별이 남자거나 또는 나이가 28세 이상인 사람 추출
#
print(df[(df["성별"] == "여자") & (df["키"] >= 160)])

print(df[(df["성별"] == "남자") | (df["나이"] >= 28)])
df_m = df[(df["성별"] == "남자") | (df["나이"] >= 28)]

# reset_index: index를 0부터 다시 생성!(깔끔하게)
#  - inplace=True: 원본값을 바로 변경? True(변경)
#  - inplace=False: 원본값을 copy해서 사용! 결과 확인 후 반드시 저장(변수) 필요!
df_m.reset_index(inplace=True)
print(df_m)

# DataFrame: 2차원(행x열)
#  - drop: 행 또는 열 삭제
#  - axis(축): 0(행), 1(열)
#  - inplace=True: 해당 결과를 원본값에 적용!
df.drop("키", axis=1, inplace=True)
print(df)
