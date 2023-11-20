# matplotlib, seaborn: 그래프

import matplotlib.pyplot as plt


# plt.title("KOREA")       # 그래프 제목
# plt.plot([-1, 2, 3, 4])  # 그래프(plot)
# plt.show()               # 그래프 출력

# data(year, price)
# year = [2014, 2017, 2020, 2023]
# price = [25000, 31000, 53000, 63000]
# plt.plot(year, price, 'rs:')
# plt.axis([2013, 2024, 20000, 70000])
# plt.show()

import numpy as np

# r-- : red 점선
# g.  : green 점
# plt.plot(np.random.randn(10), "k", label="one")
# plt.plot(np.random.randn(10)*3, "r--", label="two")
# plt.plot(np.random.randn(10)*10, "g.", label="three")
# plt.legend()  # 범례
# plt.show()

# scatter: 산점도
# c(color): green
# s(size): 점의 크기
# marker='^': 점 모양(세모)
# year = [2014, 2017, 2020, 2023]
# price = [25000, 31000, 53000, 63000]
# plt.scatter(year, price, c='g', s=50, marker='^')
# plt.show()

# plt.subplot(2, 2, 1)
# plt.plot(np.random.randn(10), "b--")
# plt.subplot(2, 2, 2)
# plt.plot(np.random.randn(100), "r", alpha=0.7)  # alpha(투명도)
# plt.subplot(2, 2, 3)
# plt.plot(np.random.randn(10), "y^")
# plt.subplot(2, 2, 4)
# plt.plot(np.random.randn(10), "g.")
# plt.show()

# 히스토그램
# numbers = [5, 4, 4, 1, 6, 3, 4, 1, 2, 2]
# plt.hist(numbers)
# plt.show()

# 상자그림(box-plot)
#  - boxplot의 가장 가운데 선은 중앙값
#  - boxplot은 이상값(outlier)을 감지 할 수 있음
#  *이상값?
#   - 이상한값(남:1, 여:2) → 1과 2 이외의 숫자?(무슨 의미: 잘못됨)
#   - 평균에서 많이 벗어난 값 → 남성키 평균이 175cm, 어떤 남성 키 220cm

# numbers = [0, 1.4, 1.6, 1.8, 1.85, 1.9, 2.2, 2.5, 5.7, 9]
# plt.boxplot(numbers)
# plt.show()

subject = ["KOR", "ENG", "MATH"]
grade = [85, 76, 55]

plt.title("Report")    # 그래프 제목
plt.xlabel("Subject")  # x축 라벨
plt.ylabel("Grade")    # y축 라벨


plt.bar(subject, grade)  # 막대 그래프
plt.ylim(0, 100)   # y축 범위
plt.text(0, 90, "Good!")  # 조건 달성시 text 출력
plt.show()

