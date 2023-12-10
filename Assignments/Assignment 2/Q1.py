from sympy import symbols, exp, integrate

lambda_b, lambda_s, t = symbols('lambda_b lambda_s t')


pdf_T1 = (lambda_b + lambda_s) * exp(-(lambda_b + lambda_s) * t)
E_T1 = integrate(t * pdf_T1, (t, 0, float('inf')))

pdf_T2 = lambda_b * lambda_s / (lambda_b + lambda_s) * exp(-lambda_b * t) * exp(-lambda_s * t)
E_T2 = integrate(t * pdf_T2, (t, 0, float('inf')))

E_T1, E_T2