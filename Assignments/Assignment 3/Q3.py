from scipy.special import factorial

lambda_ = 1
mu = 4
c = 2

rho = lambda_ / (c * mu)

p0 = (sum([(c * rho)**n / factorial(n) for n in range(c)]) + 
      ((c * rho)**c / factorial(c)) * (1 / (1 - rho))) ** -1

l = (rho * (c * rho)**c / (factorial(c) * (1 - rho)**2)) * p0 + c * rho

lq = (rho * (c * rho)**c / (factorial(c) * (1 - rho)**2)) * p0

w = l / lambda_

wq = lq / lambda_

idle_time_percentage = (1 - rho) * 100

print(l, w * 60, idle_time_percentage)
# 0.25396825396825395 15.238095238095237 87.5