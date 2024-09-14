import matplotlib.pyplot as plt

# 預設數據，格式為 [(名稱, 相對市場佔有率, 市場增長率)]
data = [
    ('Product A', 0.8, 0.6),
    ('Product B', 0.3, 0.7),
    ('Product C', 0.2, 0.4),
    ('Product D', 0.6, 0.3)
]

# 創建圖形對象
fig, ax = plt.subplots()

# 設置X軸和Y軸的範圍 (0到1之間)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# 添加水平和垂直的分割線，將圖分成四個象限
ax.axhline(0.5, color='black', lw=1)  # 水平線
ax.axvline(0.5, color='black', lw=1)  # 垂直線

# 標註四個象限的名稱，縮小字體並放置在象限左上角
ax.text(0.51, 0.99, 'Question Marks', fontsize=8, ha='left', va='top')
ax.text(0.01, 0.99, 'Stars', fontsize=8, ha='left', va='top')
ax.text(0.51, 0.49, 'Dogs', fontsize=8, ha='left', va='top')
ax.text(0.01, 0.49, 'Cash Cows', fontsize=8, ha='left', va='top')

# 設置標題和標籤
ax.set_title('BCG Matrix')
ax.set_xlabel('Relative Market Share ')
ax.set_ylabel('Market Growth Rate ')

# 隱藏X軸和Y軸的刻度線
ax.set_xticks([])
ax.set_yticks([])

# 根據輸入數據在矩陣中添加業務單位的位置並標註座標 (右下方)
for name, x, y in data:
    ax.scatter(x, y, s=100, color='blue')  # 用藍色點標出業務單位的位置
    ax.text(x + 0.02, y - 0.02, f"{name}\n({x:.2f}, {y:.2f})", fontsize=10, ha='left', va='top')  # 在點的右下方添加名稱及座標

# 顯示圖表
plt.show()
