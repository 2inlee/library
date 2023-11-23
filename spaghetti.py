import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 난수 생성을 위한 시드 설정
np.random.seed(0)

# 랜덤 데이터 생성
data = np.random.randn(100, 2)
a, b = data[:, 0], data[:, 1]

# 2x2 서브플롯 생성
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 첫 번째 서브플롯: 두 변수의 평균과 중앙값에 대한 막대 그래프
axes[0, 0].bar('Mean', [np.mean(a), np.mean(b)], color=['blue', 'green'], alpha=0.7)
axes[0, 0].bar('Median', [np.median(a), np.median(b)], color=['blue', 'green'], alpha=0.7)
axes[0, 0].set_title('평균과 중앙값')

# 두 번째 서브플롯: 상관 계수 히트맵
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1])
axes[0, 1].set_title('상관 분석')

# 세 번째 서브플롯: 두 변수의 히스토그램
axes[1, 0].hist(a, bins=15, color='blue', alpha=0.7, label='변수 1')
axes[1, 0].hist(b, bins=15, color='green', alpha=0.7, label='변수 2')
axes[1, 0].legend()
axes[1, 0].set_title('변수의 히스토그램')

# 네 번째 서브플롯: 두 변수 간의 산점도
axes[1, 1].scatter(a, b, alpha=0.7)
axes[1, 1].set_xlabel('변수 1')
axes[1, 1].set_ylabel('변수 2')
axes[1, 1].set_title('변수 1 대 변수 2 산점도')

# 레이아웃 조정 및 그래프 표시
plt.tight_layout()
plt.show()
