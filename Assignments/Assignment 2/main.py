import random
import matplotlib.pyplot as plt
import os

# توزیع‌های زمان بین ورودها و زمان سرویس
interarrival_distribution = {1: 0.20, 2: 0.35, 3: 0.15, 4: 0.30}
service_time_distribution_able = {1: 0.15, 2: 0.25, 3: 0.40, 4: 0.20}
service_time_distribution_baker = {3: 0.45, 4: 0.30, 9: 0.15, 11: 0.10}

# تابعی برای تولید زمان بین ورودها مطابق با توزیع داده شده
def generate_interarrival_time(distribution):
    rnd = random.random()
    for time, probability in distribution.items():
        if rnd < probability:
            return time
        rnd -= probability

# تابعی برای تولید زمان سرویس برای هر سرور
def generate_service_time(distribution):
    rnd = random.random()
    for time, probability in distribution.items():
        if rnd < probability:
            return time
        rnd -= probability

# تعداد کل مشتریان
num_customers = 100

# متغیرهای مربوط به سرورها
servers = {
    'able': {'idle_time': 0, 'service_end': 0, 'utilization_times': [], 'distribution': service_time_distribution_able},
    'baker': {'idle_time': 0, 'service_end': 0, 'utilization_times': [], 'distribution': service_time_distribution_baker}
}

# زمان‌های بین ورود مشتریان و زمان ورود آنها
interarrival_times = [generate_interarrival_time(interarrival_distribution) for _ in range(num_customers)]
arrival_times = [sum(interarrival_times[:i+1]) for i in range(num_customers)]

# شبیه‌سازی
for i in range(num_customers):
    current_time = arrival_times[i]
    
    for server_name in servers:
        server = servers[server_name]
        if current_time >= server['service_end']:
            server['idle_time'] += current_time - server['service_end']
            service_time = generate_service_time(server['distribution'])
            server['service_end'] = current_time + service_time
        server['utilization_times'].append((current_time, 1 - (server['idle_time'] / current_time)))

if not os.path.exists('charts'):
    os.makedirs('charts')

# تابع برای ترسیم نمودارهای مربوط به سرور
def plot_server_utilization(server_name, server_data):
    times, util = zip(*server_data['utilization_times'])
    idle_times = [1 - u for u in util]
    
    plt.figure(figsize=(12, 6))
    
    # نمودار استفاده
    plt.subplot(1, 2, 1)
    plt.plot(times, util, label=f'{server_name.capitalize()} Utilization')
    plt.xlabel('Time')
    plt.ylabel('Utilization')
    plt.title(f'{server_name.capitalize()} Server Utilization Over Time')
    plt.legend()
    
    # ذخیره نمودار استفاده
    plt.savefig(f'charts/{server_name}_utilization.png')
    
    # نمودار زمان بیکاری
    plt.subplot(1, 2, 2)
    plt.plot(times, idle_times, label=f'{server_name.capitalize()} Idle Time')
    plt.xlabel('Time')
    plt.ylabel('Idle Time Percentage')
    plt.title(f'{server_name.capitalize()} Server Idle Time Over Time')
    plt.legend()
    
    plt.tight_layout()
    
    # ذخیره نمودار زمان بیکاری و نمایش نمودار
    plt.savefig(f'charts/{server_name}_idle_time.png')
    plt.show()

# تابعی برای محاسبه میانگین استفاده و زمان بیکاری
def calculate_utilization_and_idle_time(server_data, total_time):
    total_utilization = sum(util for _, util in server_data['utilization_times'])
    average_utilization = total_utilization / len(server_data['utilization_times'])
    average_idle_time = 1 - average_utilization
    print(f"{server_data['name']} Average Utilization: {average_utilization:.2f}")
    print(f"{server_data['name']} Average Idle Time: {average_idle_time:.2f}")

# نمودارهای استفاده و زمان بیکاری سرورها
for name, data in servers.items():
    data['name'] = name  # اضافه کردن نام سرور به داده‌ها برای استفاده در تابع
    plot_server_utilization(name, data)
    calculate_utilization_and_idle_time(data, arrival_times[-1])

# نمودارهای استفاده و زمان بیکاری سرورها
for name, data in servers.items():
    data['name'] = name  # اضافه کردن نام سرور به داده‌ها برای استفاده در تابع
    plot_server_utilization(name, data)
    calculate_utilization_and_idle_time(data, arrival_times[-1])