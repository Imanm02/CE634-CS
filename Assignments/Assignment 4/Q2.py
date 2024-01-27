from sympy import solve, ln

# تعریف متغیرها
a = symbols('a')
λ = 1  # مقدار λ را برای محاسبه نمونه 1 در نظر می‌گیریم

# محاسبه F(1) برای x <= 1
F_1 = 1**a / a

# محاسبه C برای x > 1
C = solve(F_1 - (-λ**(-λ - 1) / ln(λ)) + C, C)[0]

# حل معادله F(x) = u برای x > 1
u = symbols('u')
F_x = -λ**(-λ * x - 1) / ln(λ) + C
x_solution = solve(F_x - u, x)

print(F_1)
print(C, x_solution)