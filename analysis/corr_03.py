import matplotlib.pyplot as plt
import pandas as pd

engListening = [30, 60, 90, 31, 32, 69, 92, 99]
engScore = [70, 80, 90, 70, 71, 85, 90, 92]
engClass = [60, 120, 120, 60, 60, 180, 120, 120]
engReading = [40, 45, 60, 20, 15, 70, 60, 80]

data3 = {
    "engListening": engListening,
    "engScore": engScore,
    "engClass": engClass,
    "engReading": engReading
}
df3 = pd.DataFrame(data3)

pearson_coef = df3.corr(method="pearson")
print(pearson_coef)
print("="*100)
spearman_coef = df3.corr(method="spearman")
print(spearman_coef)
print("="*100)
kendall_coef = df3.corr(method="kendall")
print(kendall_coef)
