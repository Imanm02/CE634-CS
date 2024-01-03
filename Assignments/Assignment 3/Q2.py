from scipy import stats
import numpy as np

random_numbers = [0.05, 0.08, 0.14, 0.24, 0.33, 0.33, 0.39, 0.41, 0.44, 0.53, 0.56, 0.58, 0.63, 0.73, 0.76, 0.83, 0.84, 0.88, 0.88, 0.93]

ks_statistic, ks_p_value = stats.kstest(random_numbers, 'uniform')

bins = np.linspace(0, 1, 11)
observed_frequencies, _ = np.histogram(random_numbers, bins)

num_bins = len(bins) - 1
expected_frequencies = [len(random_numbers)/num_bins] * num_bins

expected_frequencies[-1] += len(random_numbers) - sum(expected_frequencies)

chi_square_statistic, chi_square_p_value = stats.chisquare(observed_frequencies, expected_frequencies)

print(ks_statistic)
print(ks_p_value)
print(chi_square_statistic)
print(chi_square_p_value)