import pandas as pd
import numpy as np

# داده‌های جدول
data = {
    "Interval": ["15-30", "30-45", "45-60", "60-90", "90-120", "120-180", "180-300"],
    "Frequency": [10, 20, 25, 35, 30, 20, 10]
}

# تبدیل داده‌ها به DataFrame
df = pd.DataFrame(data)

# محاسبه فراوانی کل
total_frequency = df['Frequency'].sum()

# محاسبه فراوانی نسبی
df['Relative Frequency'] = df['Frequency'] / total_frequency

# محاسبه توزیع تجمعی
df['Cumulative Distribution'] = df['Relative Frequency'].cumsum()

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