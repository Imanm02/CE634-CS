from math import factorial

# مقادیر برای دو باجه سنتی
lambda_ = 1000  # نرخ ورودی خودروها
mu = 600  # نرخ خدمت دهی هر باجه
c = 2  # تعداد باجه‌ها

# محاسبه نرخ استفاده برای هر باجه
rho = lambda_ / (c * mu)

# محاسبه P0
P0 = sum([(c * rho)**k / factorial(k) for k in range(c)]) + (c * rho)**c / (factorial(c) * (1 - rho))
P0 = 1 / P0

# محاسبه زمان انتظار
W = P0 * rho / (c * mu * (1 - rho)**2) + 1 / mu
W_hour = W  # زمان انتظار در ساعت
W_seconds = W * 3600  # تبدیل زمان انتظار به ثانیه

print(W_hour, W_seconds)
# 0.00393939393939394 14.181818181818183