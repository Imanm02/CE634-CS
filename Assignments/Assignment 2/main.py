import numpy as np
import markov

P = [
    [0.3, 0.5, 0.1, 0.1],
    [0.5, 0.3, 0.1, 0.1],
    [0.2, 0.2, 0.2, 0.4],
    [0.4, 0.4, 0.2, 0]
]

pi = [0.4, 0.3, 0.2, 0.1]

mc = markov.MarkovChain(P, pi)

kabab_count = 0
kebab_count = 0
fillet_count = 0
veggie_count = 0

# Simulate the behavior of the student over time
for i in range(10):
    # Get the current state of the student
    state = mc.get_state()
    print("Day", i+1, ":", state)
    # Update the count for the current meal
    if state == "kabab":
        kabab_count += 1
    elif state == "kebab":
        kebab_count += 1
    elif state == "fillet":
        fillet_count += 1
    else:
        veggie_count += 1
    # Move to the next state according to the transition matrix
    mc.move_to_next_state()

# Calculate the probability of each meal being chosen on a given day
kabab_prob = kabab_count / 10
kebab_prob = kebab_count / 10
fillet_prob = fillet_count / 10
veggie_prob = veggie_count / 10

print("Probability of kabab:", kabab_prob)
print("Probability of kebab:", kebab_prob)
print("Probability of fillet:", fillet_prob)
print("Probability of veggie:", veggie_prob)

def calculate_state_probability(p0, transition_matrix, N, s):
    """
    محاسبه احتمال استیت s در روز N ام با استفاده از بردار احتمال اولیه p0 و ماتریس انتقال
    """
    current_probabilities = np.array(p0)
    for _ in range(N):
        current_probabilities = np.dot(current_probabilities, transition_matrix)
    return current_probabilities[s]

# تعریف بردار احتمال اولیه و ماتریس انتقال
initial_probabilities = [0.4, 0.3, 0.2, 0.1]
transition_matrix = [
    [0.3, 0.5, 0.1, 0.1],
    [0.5, 0.3, 0.1, 0.1],
    [0.2, 0.2, 0.2, 0.4],
    [0.4, 0.4, 0.2, 0]
]

# محاسبه احتمال انتخاب جوجه کباب در روز 777ام
probability_chicken_kebab_day_777 = calculate_state_probability(initial_probabilities, transition_matrix, 777, 1)  # جوجه کباب دومین غذا است

import matplotlib.pyplot as plt

days = range(10, 10001, 10) # روزهای ۱۰ تا ۱۰۰۰۰

# احتمالات انتخاب جوجه کباب در روزهای مختلف
probabilities_chicken_kebab = [calculate_state_probability(initial_probabilities, transition_matrix, day, 1) for day in days]

#print(probabilities_chicken_kebab)

# نمایش نمودار
plt.plot(days, probabilities_chicken_kebab)
plt.xlabel('Day')
plt.ylabel('Probability of Chicken Kebab')
plt.title('Probability of Chicken Kebab over Time')
plt.show()

def simulate_markov_chain(transition_matrix, N, num_simulations):
    """
    شبیه‌سازی روند زنجیره مارکوف برای N روز و num_simulations بار
    """
    num_states = len(transition_matrix)
    state_counts = np.zeros(num_states)
    for _ in range(num_simulations):
        current_state = np.random.choice(num_states)
        for _ in range(N):
            current_state = np.random.choice(num_states, p=transition_matrix[current_state])
        state_counts[current_state] += 1
    return state_counts / num_simulations

# شبیه‌سازی برای روز 777ام و 1000 بار
simulation_results_777 = simulate_markov_chain(transition_matrix, 777, 1000)
approx_probability_chicken_kebab_day_777 = simulation_results_777[1] # جوجه کباب دومین غذا است

print(simulation_results_777)
print(approx_probability_chicken_kebab_day_777)