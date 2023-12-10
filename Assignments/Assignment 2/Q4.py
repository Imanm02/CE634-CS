import networkx as nx
import matplotlib.pyplot as plt

# تعریف ماتریس انتقال
transition_matrix = [
    [4/6, 2/6, 0],
    [1/6, 0, 5/6],
    [0, 0, 1]
]

# ایجاد یک زنجیره مارکوف با استفاده از NetworkX
G = nx.DiGraph()

# اضافه کردن گره‌ها و یال‌ها به گراف
states = ['A', 'B', 'C']
for i, origin_state in enumerate(states):
    for j, destination_state in enumerate(states):
        probability = transition_matrix[i][j]
        if probability > 0:
            G.add_edge(origin_state, destination_state, weight=probability)

# تنظیم موقعیت‌های گره‌ها
pos = {'A': (0, 0), 'B': (1, 0.5), 'C': (2, 0)}

# رسم گراف
edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in G.edges(data=True)}
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=15, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# نمایش گراف
plt.title("Markov Chain Plot")
plt.show()