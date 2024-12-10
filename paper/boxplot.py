import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('13_bus_up2.csv')
# travel_time의 boxplot 생성
plt.figure(figsize=(10, 6))
plt.boxplot(df['travel_time'], vert=False, patch_artist=True)
plt.title("Boxplot of Travel Time")
plt.xlabel("Travel Time")
plt.show()