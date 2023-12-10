import numpy as np

def calculate_state_probability(initial_probabilities, transition_matrix, N):
    """
    محاسبه احتمال حالت در روز ورودی با استفاده از بردار احتمال اولیه و ماتریس انتقال
    """
    current_probabilities = np.array(initial_probabilities)
    for _ in range(N):
        current_probabilities = np.dot(current_probabilities, transition_matrix)
    return current_probabilities

# تعریف بردار احتمال اولیه و ماتریس انتقال
initial_probabilities = [0.3, 0.2, 0.3, 0.2]
transition_matrix = [
    [0.3, 0.5, 0.1, 0.1],
    [0.5, 0.3, 0.1, 0.1],
    [0.2, 0.2, 0.2, 0.4],
    [0.4, 0.4, 0.2, 0]
]

# محاسبه احتمال انتخاب جوجه کباب در روز 777ام
probabilities_day_777 = calculate_state_probability(initial_probabilities, transition_matrix, 777)
probability_chicken_kebab_day_777 = probabilities_day_777[1] # جوجه کباب دومین غذا است
