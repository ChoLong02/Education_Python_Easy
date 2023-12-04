# 상관관계 분석(Correlation analysis: Corr)
#  - 두 변수(특징) 사이 관계의 강도와 바향을 파악하는 통계기법
#  예) 넷플릭스 시청시간과 학점
#     시청시간↑ 학점↓ = 음의 상관관계
#     기온과 아이스크림 판매량
#     기온↑ 판매량↑ = 양의 상관관계

# ** 상관계수(=상관분석 값)
#  - -1~1 사이의 값
#  - -1과1에 가까울수록 상관정도가 높음
#  - 0에 가까울수록 상관없음
#  - 1에 가까울수록 양의 상관관계(정비례)
#  - -1에 가까울수록 음의 상관관계(반비례)

# ** 상관분석 종류
#  1.피어슨
#   - 가장 일반적인 상관분석 방법
#   - 두 연속 변수간의 선형 관계를 측정
#   - 스피어만보다 이상치에 민감하게 반응함
#  2.스피어만
#   - 두 변수가 정규성을 보이지 않는 경우 사용
#   - 선형여부에 상관 없이 단조 연관성 측정
#  3.켄달
#   - 스피어만과 비슷하나 표본 데이터가 적고 동점이 많은 경우 사용
#   - 두 변수 간의 순위를 비교하여 연관성 계산
#   - 한 변수가 증가할 때 다른 변수가 함께 증가하는 횟수와 감소하는
#     횟수를 측정하여 횟수의 차이를 상관관계로 표현
#   - 상관이 없음(+-0~+-0.4)
#   - 약한 상관관계(+-0.4~+-0.7)
#   - 강한 상관관계(+-0.7~)

#   - 0.5 ↑ 강한 상관관계
#   - 0.5 ↓ 약한 상관관계


# 단조 관계(곡선): 두 변수가 상대적인 방향으로 이동하는 경향은 같지만
#                 반드시 일정한 비율로 변화하는 것은 아님

# 단조+선형관계(직선)

import pandas as pd
engListening = [30, 60, 90]
engScore = [70, 80, 90]

# 데이터프레임 만들기(표)
data = {"engListening": engListening,
        "engScore": engScore}
df = pd.DataFrame(data)

# 상관분석(피어슨)
coef = df.corr(method="pearson")
print(coef)



