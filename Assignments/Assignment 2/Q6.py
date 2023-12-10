import numpy as np
import matplotlib.pyplot as plt

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

print(probability_chicken_kebab_day_777) # = 0.3750000000000001

days = range(10, 10001, 10) # روزهای ۱۰ تا ۱۰۰۰۰

# احتمالات انتخاب جوجه کباب در روزهای مختلف
probabilities_chicken_kebab = [calculate_state_probability(initial_probabilities, transition_matrix, day, 1) for day in days]

print(probabilities_chicken_kebab)

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

print(simulation_results_777) # = [0.381 0.367 0.114 0.138]
print(approx_probability_chicken_kebab_day_777) # = 0.367

# د) مقایسه نتایج محاسباتی و شبیه‌سازی
simulation_results_777_10000 = simulate_markov_chain(transition_matrix, 777, 10000)
approx_probability_chicken_kebab_day_777_10000 = simulation_results_777_10000[1]

# مقایسه خطای دو شبیه‌سازی
error_1000 = abs(probability_chicken_kebab_day_777 - approx_probability_chicken_kebab_day_777)
error_10000 = abs(probability_chicken_kebab_day_777 - approx_probability_chicken_kebab_day_777_10000)

print(f"Probability of choosing Chicken Kebab on day 777: {probability_chicken_kebab_day_777}")
# Probability of choosing Chicken Kebab on day 777: 0.3750000000000001

print(f"Approximate probability of choosing Chicken Kebab on day 777 (Simulation with 1000 runs): {approx_probability_chicken_kebab_day_777}")
# Approximate probability of choosing Chicken Kebab on day 777 (Simulation with 1000 runs): 0.367

print(f"Approximate probability of choosing Chicken Kebab on day 777 (Simulation with 10000 runs): {approx_probability_chicken_kebab_day_777_10000}")
# Approximate probability of choosing Chicken Kebab on day 777 (Simulation with 10000 runs): 0.3774

print(f"Error in simulation with 1000 runs: {error_1000}")


print(f"Error in simulation with 10000 runs: {error_10000}")



Error in simulation with 1000 runs: 0.008000000000000118
Error in simulation with 10000 runs: 0.002399999999999902