from scipy.stats import chisquare

def clcg(seed, a, c, m):
    """ تابع تولید کننده اعداد شبه تصادفی با استفاده از الگوریتم CLCG """
    while True:
        seed = (a * seed + c) % m
        yield seed / m

# نمونه استفاده از تابع
clcg_generator = clcg(seed=1, a=1103515245, c=12345, m=2**31)
next(clcg_generator)  # برای تولید عدد بعدی

def xor_shift(seed):
    """ تابع تولید کننده اعداد شبه تصادفی با استفاده از الگوریتم xor-shift """
    x = seed
    x ^= (x << 13) & 0xFFFFFFFF
    x ^= (x >> 17)
    x ^= (x << 5) & 0xFFFFFFFF
    return x

# نمونه استفاده از تابع
random_number = xor_shift(seed=123456789)

def chi_square_test(data):
    """ تابع انجام تست chi-square بر روی داده‌های ورودی """
    stat, p_value = chisquare(data)
    return stat, p_value

# نمونه استفاده از تابع
data = [20, 30, 25, 25]  # داده‌های شبه تصادفی
stat, p_value = chi_square_test(data)
print(f"Chi-Square Statistic: {stat}, P-value: {p_value}")