# 인공지능
#  - 기계(AI) 스스로 규칙을 찾는 알고리즘
#  - 기존: 입력(인간이만든 규칙 + 데이터) -> 결과
#  - AI: 입력(데이터, 결과) -> 규칙 생성
#    * 결과(=정답)

# 기존
#   - 인간이 만든 규칙: 초록불 건너시오, 빨간불 Stop
#   - 데이터: 초록불 or 빨간불
#   - 결과: 건너기 or Stop

# 인공지능
#   - 입력: 데이터와 정답
#         1 초록불   건너기
#         2 빨간불   멈춤
#         3 빨간불   멈춤
#         4 초록불   건너기
#         5 초록불   건너기
# 데이터와 정답을 기계(AI)에 입력으로 주면 기계가
# 스스로 공부를 해서 규칙을 생성
# * 양질의 데이터가 많으면 좋다.

# 인공지능 산업 키우기 위해서는 반드시 양질의 데이터가 필요!
#  - AI허브(국가) 참고

# 인공지능 2가지 분류
#  - 머신러닝 → 딥러닝

#  머신러닝: 다양한(통계학, 수학, 기타 등등) 알고리즘을 활용해서
#           데이터와 정답간의 패턴을 찾고 규칙을 생성하는 방법
#           (KNN, Naive-basian, decision tree, SVM,
#            K-means Clustering, Apriori, 기타 등등)

# 앙상블(Ensemble): 머신러닝 모델 여러개를 결합해서 사용하는 방법
#   1.배깅(Bagging)
#   2.부스팅(Boosting)
#   3.보팅(Voting)
#   4.스태킹(Stacking)

#  딥러닝: 인공신경망(인간의 학습방법을 모토)
#          - 지금 현존하는 대부분의 인공지능 딥러닝!
#          - 알파고?, Chat-GPT, Dall-E


# 딥러닝 학습방법
# 1.세트(데이터+정답)를 모델에 입력으로 넣기
# 2.모델은 입력받은 세트를 사용해서 규칙생성(학습 완료)
# 3.학습이 완료된 모델에 평가 데이터를 넣고 평가
# 4.평가결과 Good: 실전에서 사용
#            Bad: 재학습


# scikit-learn(머신러닝 끝판왕)
# 1.수집+저장
from sklearn.datasets import load_wine
wine = load_wine()

import pandas as pd
import numpy as np

# 3.탐색적 데이터 분석
wine_feature = wine.data  # 데이터
wine_label = wine.target  # 정답
df_wine = pd.DataFrame(data=wine_feature,
                       columns=[wine.feature_names])
df_wine["label"] = wine_label
print(wine.DESCR)
print(df_wine)

# 4.데이터 전처리
from sklearn.model_selection import train_test_split
# 데이터 -> 학습과 평가
df_wine = df_wine.astype(({"label": "int"}))
train, test = train_test_split(df_wine,   # 학습/평가로 나눌 데이터
                               test_size=0.3,    # 7:3 비율
                               random_state=0,   # 랜덤값 고정
                               stratify=df_wine["label"])  # 7:3비율 랜덤(Label 비율에 맞추기)

# 와인데이터 -> 특징(14개) = 데이터 특징(13개) + 정답(1개)
train_X = train[train.columns[0:13]]  # 데이터 특징(13개)
train_Y = train[train.columns[13:]]   # 정답(1개)

test_X = test[test.columns[0:13]]     # 데이터 특징(13개)
test_Y = test[test.columns[13:]]      # 정답(1개)

# 5.베이스라인 모델 개발하기
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


model = KNeighborsClassifier()  # 모델 생성
model.fit(train_X, train_Y)     # 모델 학습(규칙 생성)
#         X(데이터), Y(정답) -> model -> model(+규칙)

# 6.평가
# model이 test_X(13개특징) -> Class1 or Class2 or Class3
pred_knn = model.predict(test_X)  # 평가 데이터만 입력, 정답X
print("KNN 알고리즘 분류 정확도:",
      metrics.accuracy_score(pred_knn, test_Y))

