from scipy.special import factorial

lambda_ = 1  # نرخ ورود بیماران (بیمار در ساعت)
mu = 4       # نرخ خدمات پزشکان (بیمار در ساعت)
c = 2        # تعداد پزشکان

# محاسبه فاکتور استفاده از پزشکان
rho = lambda_ / (c * mu)

# محاسبه احتمال عدم وجود بیمار در سیستم
p0 = (sum([(c * rho)**n / factorial(n) for n in range(c)]) + 
      ((c * rho)**c / factorial(c)) * (1 / (1 - rho))) ** -1

# محاسبه میانگین تعداد بیماران در سیستم
l = (rho * (c * rho)**c / (factorial(c) * (1 - rho)**2)) * p0 + c * rho

# محاسبه میانگین تعداد بیماران در صف
lq = (rho * (c * rho)**c / (factorial(c) * (1 - rho)**2)) * p0

# محاسبه میانگین زمان انتظار در سیستم
w = l / lambda_

# محاسبه میانگین زمان انتظار در صف
wq = lq / lambda_

# محاسبه درصد زمان بیکاری پزشکان
idle_time_percentage = (1 - rho) * 100

print(l, w * 60, idle_time_percentage)
# 0.25396825396825395 15.238095238095237 87.5