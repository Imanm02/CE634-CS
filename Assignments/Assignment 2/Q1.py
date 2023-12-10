from sympy import symbols, exp, integrate

# Define the symbols
lambda_b, lambda_s, t = symbols('lambda_b lambda_s t')

# For E[T1], we are looking for the first event in either of the Poisson processes
# The combined rate of events for both processes is lambda_b + lambda_s
# The probability density function (PDF) for the first event in a Poisson process is lambda * exp(-lambda * t)
# Therefore, the PDF for the first event in either process is (lambda_b + lambda_s) * exp(-(lambda_b + lambda_s) * t)
# E[T1] is the integral of t times this PDF over all t from 0 to infinity

pdf_T1 = (lambda_b + lambda_s) * exp(-(lambda_b + lambda_s) * t)
E_T1 = integrate(t * pdf_T1, (t, 0, float('inf')))

# For E[T2], we are interested in the time when both types of bread have been produced at least once
# This is a bit more complex, as it involves the minimum of two independent exponential distributions
# The PDF for the minimum of two independent exponential variables is lambda_b * lambda_s / (lambda_b + lambda_s) * exp(-lambda_b * t) * exp(-lambda_s * t)
# E[T2] is the integral of t times this PDF over all t from 0 to infinity

pdf_T2 = lambda_b * lambda_s / (lambda_b + lambda_s) * exp(-lambda_b * t) * exp(-lambda_s * t)
E_T2 = integrate(t * pdf_T2, (t, 0, float('inf')))

E_T1, E_T2