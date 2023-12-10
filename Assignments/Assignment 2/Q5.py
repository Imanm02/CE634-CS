import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# ماتریس انتقال
P = np.array([
    [1/4, 1/4, 1/2],
    [1/3, 0, 2/3],
    [0, 1/2, 1/2]
])

# رسم نمودار زنجیره مارکوف
G = nx.DiGraph()

# اضافه کردن گره‌ها و یال‌ها به نمودار با توجه به احتمالات انتقال
for i in range(3):
    for j in range(3):
        if P[i, j] > 0:
            G.add_edge(i+1, j+1, weight=P[i, j])

# موقعیت گره‌ها برای نمایش بهتر نمودار
pos = {1: (0, 0), 2: (1, 0.5), 3: (2, 0)}

# رسم نمودار با نمایش وزن یال‌ها
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title('Markov Chain Plot')
plt.show()

# محاسبه P(X1 = 3, X2 = 2, X3 = 1)
# از آنجایی که P(X1 = 1) = P(X1 = 2) = P(X1 = 3) = 1/3 است
probability_x1_3_x2_2_x3_1 = (1/3) * P[2, 1] * P[1, 0]
probability_x1_3_x2_2_x3_1