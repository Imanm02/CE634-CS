import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

samples1 = np.array([
    0.685031, 1.734970, 1.147495, 0.955480, 0.411855, 0.411821, 0.244620,
    1.418179, 0.958688, 1.109617, 0.144220, 1.871779, 1.336574, 0.488557,
    0.447972, 0.450124, 0.602290, 0.862513, 0.752022, 0.586705, 0.972816,
    0.387601, 0.587806, 0.675483, 0.780343, 1.240135, 0.471949, 0.849723,
    0.947367, 0.218091, 0.967126, 0.432390, 0.259353, 1.724438, 1.835928,
    1.285430, 0.602734, 0.320589, 1.073662, 0.761637, 0.360766, 0.826769,
    0.187066, 1.549330, 0.547227, 1.042236, 0.611185, 0.856803, 0.889508,
    0.452094
])

sorted_samples1 = np.sort(samples1)

shape_param = 1.6
scale_param = 2

theoretical_quantiles_weibull = stats.weibull_min.ppf((np.arange(1, len(samples1) + 1) - 0.5) / len(samples1), shape_param, scale=scale_param)

plt.figure(figsize=(8, 6))
plt.scatter(theoretical_quantiles_weibull, sorted_samples1, edgecolor='k', facecolor='white')
plt.plot(theoretical_quantiles_weibull, theoretical_quantiles_weibull, 'r--')
plt.xlabel('Theoretical Quantiles (Weibull)')
plt.ylabel('Sample Quantiles')
plt.title('Q-Q Plot for Weibull Distribution (File 1 Data)')
plt.grid(True)
plt.show()

mean_normal = 0
variance_normal = 2
std_dev_normal = np.sqrt(variance_normal)

theoretical_quantiles_normal = stats.norm.ppf((np.arange(1, len(samples1) + 1) - 0.5) / len(samples1), mean_normal, std_dev_normal)

plt.figure(figsize=(8, 6))
plt.scatter(theoretical_quantiles_normal, sorted_samples1, edgecolor='k', facecolor='white')
plt.plot(theoretical_quantiles_normal, theoretical_quantiles_normal, 'r--')
plt.xlabel('Theoretical Quantiles (Normal)')
plt.ylabel('Sample Quantiles')
plt.title('Q-Q Plot for Normal Distribution (File 1 Data)')
plt.grid(True)
plt.show()

samples2 = np.array([
    0.927133, 1.116499, 1.027898, 0.990933, 0.837431, 0.837417, 0.754568,
    1.072374, 0.991598, 1.021021, 0.678899, 1.133577, 1.059738, 0.866529,
    0.851629, 0.852445, 0.903569, 0.970852, 0.944596, 0.898843, 0.994503,
    0.827327, 0.899180, 0.924534, 0.951606, 1.043984, 0.860556, 0.967956,
    0.989245, 0.737442, 0.993337, 0.845620, 0.763446, 1.115140, 1.129201,
    1.051501, 0.903702, 0.796507, 1.014317, 0.946999, 0.815540, 0.962669,
    0.715153, 1.091513, 0.886408, 1.008308, 0.906222, 0.969563, 0.976855,
    0.853190
])

sorted_samples1 = np.sort(samples1)
sorted_samples2 = np.sort(samples2)

plt.figure(figsize=(8, 6))
plt.scatter(sorted_samples1, sorted_samples2, edgecolor='k', facecolor='blue')
plt.plot([min(min(sorted_samples1), min(sorted_samples2)), max(max(sorted_samples1), max(sorted_samples2))], 
         [min(min(sorted_samples1), min(sorted_samples2)), max(max(sorted_samples1), max(sorted_samples2))], 'r--')
plt.xlabel('Sample Quantiles of File 1 (X)')
plt.ylabel('Sample Quantiles of File 2 (Y)')
plt.title('Q-Q Plot Comparison Between File 1 and File 2')
plt.grid(True)
plt.show()