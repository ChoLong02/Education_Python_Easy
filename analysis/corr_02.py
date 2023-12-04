import matplotlib.pyplot as plt
import pandas as pd

engListening = [30, 60, 90, 31, 32, 69, 92, 99]
engScore = [70, 80, 90, 70, 71, 85, 90, 92]

data2 = {
    "engListening": engListening,
    "engScore": engScore
}
df2 = pd.DataFrame(data2)

plt.scatter(df2["engListening"], df2["engScore"])
plt.show()

coef = df2.corr(method="pearson")
print(coef)










