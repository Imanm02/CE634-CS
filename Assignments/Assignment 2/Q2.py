from itertools import product

# ایجاد تمام حالت های ممکن برای دو تاس
dice_4 = range(1, 5)  # تاس چهار وجهی
dice_6 = range(1, 7)  # تاس شش وجهی
all_outcomes = list(product(dice_4, dice_6))

# محاسبه احتمالات و سود/زیان برای هر حالت
profit_when_X_greater_Y = sum(2 * x for x, y in all_outcomes if x > y) / len(all_outcomes)
loss_when_X_not_greater_Y = sum(-1 for x, y in all_outcomes if x <= y) / len(all_outcomes)

# محاسبه احتمالات و سود/زیان برای هر حالت در یک پرتاب
# احتمال X > Y و سود متناظر
profit_cases = [(2 * x, 1/24) for x in dice_4 for y in dice_6 if x > y]

# احتمال X <= Y و زیان 1 دلار
loss_cases = [(-1, 1/24) for x in dice_4 for y in dice_6 if x <= y]

# امید ریاضی کلی سود برای یک پرتاب
expected_profit_per_throw = profit_when_X_greater_Y + loss_when_X_not_greater_Y

# امید ریاضی کلی سود برای 60 پرتاب
expected_total_profit_60_throws = 60 * expected_profit_per_throw

expected_profit_per_throw, expected_total_profit_60_throws