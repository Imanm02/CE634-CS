import numpy as np

# تولید 5 عدد تصادفی R_i در بازه [0, 1]
random_numbers = np.random.uniform(0, 1, 5)

# تابع برای تعیین بازه زمانی متناظر با R_i
def determine_service_time(R, df):
    for index, row in df.iterrows():
        if R <= row['Cumulative Distribution']:
            return row['Interval']
    return "نامعلوم"

# محاسبه بازه‌های زمانی برای هر R_i
service_times = [determine_service_time(R, df) for R in random_numbers]

# نتایج
print(service_times)
print(random_numbers)