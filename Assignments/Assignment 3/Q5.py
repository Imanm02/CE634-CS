from sympy import symbols, solve

# تعریف متغیرها
λ = 1000  # نرخ ورود (خودروها در ساعت)
μ1 = 1200  # نرخ سرویس دهی برای باجه اتوماتیک (خودروها در ساعت)
μ2 = 600   # نرخ سرویس دهی برای هر یک از دو باجه سنتی (خودروها در ساعت)
ρ1 = λ / μ1  # نرخ استفاده برای باجه اتوماتیک
ρ2 = λ / (2 * μ2)  # نرخ استفاده برای دو باجه سنتی

# محاسبه زمان انتظار مورد انتظار در حالت پایدار برای هر دو سناریو
# برای M/M/1
W1 = symbols('W1')
equation1 = W1 - 1 / (μ1 - λ)
expected_waiting_time_automated = solve(equation1, W1)[0]

# برای M/M/2
W2 = symbols('W2')
equation2 = W2 - 1 / (2 * μ2 - λ)
expected_waiting_time_manual = solve(equation2, W2)[0]

print(expected_waiting_time_automated)
print(expected_waiting_time_manual)