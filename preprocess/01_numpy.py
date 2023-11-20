# 데이터 분석 과정
#  1.데이터 수집   -> requests, beautifulsoup, selenium
#  2.데이터 저장   -> pymongo, MongoDB(DB)
#  3.탐색적 데이터 분석 -> pandas, matplotlib
#  4.데이터 전처리 -> numpy, pandas
#  5.데이터 분석   -> scikit-learn, tensorflow+keras, pytorch
#  6.데이터 시각화  -> matplotlib, seaborn

# 목적: 000 데이터를 분석해서 00 결과 도출
# 1,2 단계 -> 원천 데이터(Raw): 가공이 되지 않은(날 것 그대로)

# 3단계: 원천 테이터 탐색(데이터 모양, 형태, 특징 등을 탐색)
# 4단계: 전처리: 분석하기 전에 데이터를 가공(좋은 결과 도출위해)
# 5단계: 분석: 어떤 결과 도출? 분석 방법
# 6단계: 시각화: 분석결과 보기 편하게 그래프 그리기

# 넘파이(Numpy): 숫자 데이터를 포함한 벡터와 행렬 연산에 유용한 라이브러리

# 배열(Array)의 차원(Dimension)
#  1.스칼라(Scalar): 0차원, 값1개  ex) 35
#  2.벡터(Vector): 1차원, 스칼라값을 가로 또는 세로로 1열로 길게
#    ex) [1, 2, 3, 4, 5]       [가
#                               나
#                               다]
#  3.행렬(Matrix): 2차원(표)
#    ex) [[1 2 3],
#         [4 5 6],
#         [7 8 9]]
#  4.텐서(Tensor): 3차원

# Dimension(차원): 특징, 데이터의 속성의 수 또는 측정 항목
#  - 학생: 대학교, 학과, 학년, 학번, 이름, 나이, 주소, 전화번호
#  - 데이터 분석 또는 인공지능 모델 만들시 특징이 너무 많으면
#                                     (차원이 너무 크면)
#    → 차원의 저주: 성능 하락, 분석 결과 잘못 나오는 경우
#    → 해결: 특징 줄이기(=차원 감소)
#          1) 특징 추출 2) 특징 선택 3) PCA, t-SNE, 그 외 기타 등등

# import numpy -> numpy 라이브러리 사용할거에요!
# as np -> numpy를 저는 np라고 부를게요!
import numpy as np

# 리스트(벡터)를 생성하고 배열로 변환하기(Numpy 변환)
list1 = [1, 2, 3, 4]  # 벡터(Numpy Type 아님)
a = np.array(list1)   # list1 벡터를 Numpy 배열로 변환
print(type(list1))
print(type(a))

print(a)
print("a[0]", a[0])
print("a[2]", a[2])
print(f"shape: {a.shape}")
# shape: 데이터의 모양
#  - 1차원(?,)  ex) (5,)    (5) -> 스칼라(5)

# 2차원
print("=" * 50)
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(b)
print(f"2차원 Shape: {b.shape}")
print("b[0]", b[0])
print("b[0, 2]", b[0, 2])

# 배열 채우기!
print("=" * 50)
a = np.zeros(2)  # -> 배열 만들고 0으로 채우기
print(a)
b = np.zeros((2, 2))
print(b)
c = np.ones((2, 2))  # -> 배열 만들고 1로 채우기
print(c)
d = np.full((2, 2), 7)  # 0-> 배열 만들고 7로 채우기
print(d)

# 정수형, 실수형 타입 변경
print("=" * 50)
# float64 -> 실수형(소수점 있음)
a = np.array([1, 2], dtype=np.float64)
print(a.dtype)
print(a)

# 정수형 배열로 변환하기
a_i8 = a.astype(np.int8)  # -> int: 정수
print(a_i8.dtype)
print(a_i8)

# 배열 모양 바꾸기
print("=" * 50)
# arange(8) -> 0부터 7까지 1씩 증가하는 배열 생성
a = np.arange(8)
print(a)

# Shape: (8, ) ->
a.shape = (2, 4)
print(a)

# flatten() 고차원을 저차원 변경 ex) 2차원 -> 1차원
print(a.flatten())  # 이미지

# 이미지(24x24) -> flatten(): (24, 24) -> (576,)

# resize(): 배열 모양 변경
a.resize((4, 2))
print(a)

