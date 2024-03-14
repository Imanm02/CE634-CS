import numpy as np

# فرض یک ماتریس انتقال که می‌تواند منجر به وضعیت پایدار مشاهده شده شود
transition_matrix = np.array([[0.33, 0.33, 0.34],
                              [0.33, 0.34, 0.33],
                              [0.34, 0.33, 0.33]])

# بردارهای حالت اولیه
p0_a = np.array([0, 1, 0])  # برای حالت اول
p0_b = np.array([0, 0, 1])  # برای حالت دوم

# تابعی برای شبیه‌سازی فرآیند مارکوف برای تعداد زیادی گام
def simulate_markov(p0, transition_matrix, steps):
    current_state = p0
    for _ in range(steps):
        current_state = np.dot(current_state, transition_matrix)
    return current_state

# شبیه‌سازی برای تعداد زیادی گام برای نزدیک شدن به حالت پایدار
steps = 100000
steady_state_a = simulate_markov(p0_a, transition_matrix, steps)
steady_state_b = simulate_markov(p0_b, transition_matrix, steps)

print(steady_state_a, steady_state_b)

# یک حالت دیگه

# تعریف ماتریس انتقال P
P = np.array([[0.5, 0.2, 0.3],
              [0.3, 0.4, 0.3],
              [0.4, 0.1, 0.5]])

# تابع برای پیدا کردن بردار حالت پایدار
def find_steady_state(P):
    n = P.shape[0]
    A = np.transpose(P - np.identity(n))
    A = np.vstack([A, np.ones(n)])
    b = np.append(np.zeros(n), 1)
    steady_state = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, b))
    return steady_state

# محاسبه بردار حالت پایدار
steady_state = find_steady_state(P)
print("Steady State:", steady_state)