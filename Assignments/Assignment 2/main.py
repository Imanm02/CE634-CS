import numpy as np

def calculate_state_probability(initial_probabilities, transition_matrix, N):
    """
    محاسبه احتمال حالت در روز ورودی با استفاده از بردار احتمال اولیه و ماتریس انتقال
    """
    current_probabilities = np.array(initial_probabilities)
    for _ in range(N):
        current_probabilities = np.dot(current_probabilities, transition_matrix)
    return current_probabilities

