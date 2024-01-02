from scipy import stats
import numpy as np

# اعداد تصادفی داده شده
random_numbers = [0.05, 0.08, 0.14, 0.24, 0.33, 0.33, 0.39, 0.41, 0.44, 0.53, 0.56, 0.58, 0.63, 0.73, 0.76, 0.83, 0.84, 0.88, 0.88, 0.93]

# تست Kolmogorov-Smirnov
ks_statistic, ks_p_value = stats.kstest(random_numbers, 'uniform')

# تقسیم اعداد به 10 بازه برای تست Chi-Square
bins = np.linspace(0, 1, 11)
observed_frequencies, _ = np.histogram(random_numbers, bins)

# انتظارات برای توزیع یکنواخت (هر بازه یکسان)
expected_frequencies = [len(random_numbers) / len(bins)] * (len(bins) - 1)

# تست Chi-Square
chi_square_statistic, chi_square_p_value = stats.chisquare(observed_frequencies, expected_frequencies)

print(ks_statistic)
print(ks_p_value)
print(chi_square_statistic)
print(chi_square_p_value)