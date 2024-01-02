from scipy.stats import chisquare
import numpy as np

def clcg(seed, a, c, m, n):
    """ تابع تولید کننده اعداد شبه تصادفی با استفاده از الگوریتم CLCG """
    numbers = []
    for _ in range(n):
        seed = (a * seed + c) % m
        numbers.append(seed / m)
    return numbers

# تولید 1000 عدد شبه تصادفی با CLCG
clcg_numbers = clcg(seed=1, a=1103515245, c=12345, m=2**31, n=1000)

def xor_shift(seed, n):
    """ تابع تولید کننده اعداد شبه تصادفی با استفاده از الگوریتم xor-shift """
    numbers = []
    for _ in range(n):
        seed ^= (seed << 13) & 0xFFFFFFFF
        seed ^= (seed >> 17)
        seed ^= (seed << 5) & 0xFFFFFFFF
        numbers.append(seed / 0xFFFFFFFF)
    return numbers

# تولید 1000 عدد شبه تصادفی با xor-shift
xor_shift_numbers = xor_shift(seed=123456789, n=1000)

def chi_square_test(data, bins):
    """ تابع انجام تست chi-square بر روی داده‌های ورودی """
    hist, _ = np.histogram(data, bins=bins)
    stat, p_value = chisquare(hist)
    return stat, p_value

# تست chi-square برای اعداد تولید شده با CLCG
stat, p_value = chi_square_test(clcg_numbers, bins=10)
print(f"Chi-Square Statistic (CLCG): {stat}, P-value: {p_value}")

# تست chi-square برای اعداد تولید شده با xor-shift
stat, p_value = chi_square_test(xor_shift_numbers, bins=10)
print(f"Chi-Square Statistic (xor-shift): {stat}, P-value: {p_value}")