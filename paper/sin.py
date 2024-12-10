import numpy as np
import matplotlib.pyplot as plt

# x 값 범위 설정 (0에서 2π까지 100개의 점)
x = np.linspace(0, 2 * np.pi, 100)

# sin(x) 계산
y = np.sin(x)

# 그래프 그리기
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='sin(x)', color='blue')  # sin(x) 그래프
plt.title('Sine Function')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # x축 선
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # y축 선
plt.grid(alpha=0.3)  # 그리드 추가
plt.legend()  # 범례 추가
plt.show()
