from sympy import symbols, integrate, Heaviside, erf, sqrt, pi, exp

x, y = symbols('x y')

r_x = exp(-x**2 / 2) / sqrt(2 * pi)
s_x = 2 * r_x * Heaviside(x)

S_y = integrate(s_x, (x, -np.inf, y))

# محاسبه انتگرال برای E[s(Y)/(c * r(Y)) | Y <= y] به صورت سمبولیک
expected_value = integrate(s_x / r_x, (x, -np.inf, y))

print(S_y, expected_value)