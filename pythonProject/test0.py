import matplotlib.pyplot as plt
import numpy as np

# 定义雷达图的维度
categories = ['1', '2', '3', '4', '5']
N = len(categories)

# 定义各个维度上的分数
# 假设值可以根据实际情况调整
smart_edu_platform = [85, 80, 75, 70, 65]
competitor = [60, 70, 80, 85, 90]

# 将第一个值添加到最后，以封闭雷达图
smart_edu_platform += smart_edu_platform[:1]
competitor += competitor[:1]

# 计算每个维度的角度
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

# 初始化雷达图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# 绘制各个维度的轴
plt.xticks(angles[:-1], [f'{i+1}' for i in range(N)], color='black', size=12)

# 绘制y轴标签
ax.set_rlabel_position(0)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=7)
plt.ylim(0,100)

# 绘制智能幼教云平台的数据
ax.plot(angles, smart_edu_platform, linewidth=2, linestyle='solid', label='Smart Edu Platform')
ax.fill(angles, smart_edu_platform, 'b', alpha=0.1)

# 绘制竞争对手的数据
ax.plot(angles, competitor, linewidth=2, linestyle='solid', label='Competitor')
ax.fill(angles, competitor, 'r', alpha=0.1)

# 添加图例
plt.legend(loc='upper right')

# 添加标题
plt.title('Competitive Analysis Radar Chart', size=15, color='black')

# 展示图表
plt.show()
