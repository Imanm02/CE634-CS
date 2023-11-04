import random
import matplotlib.pyplot as plt

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


# تابع برای ترسیم نمودارهای مربوط به سرور
def plot_server_utilization(server_name, server_data):
    times, util = zip(*server_data['utilization_times'])
    idle_times = [1 - u for u in util]
    
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(times, util, label=f'{server_name.capitalize()} Utilization')
    plt.xlabel('Time')
    plt.ylabel('Utilization')
    plt.title(f'{server_name.capitalize()} Server Utilization Over Time')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(times, idle_times, label=f'{server_name.capitalize()} Idle Time')
    plt.xlabel('Time')
    plt.ylabel('Idle Time Percentage')
    plt.title(f'{server_name.capitalize()} Server Idle Time Over Time')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# نمودارهای استفاده و زمان بیکاری سرورها
for name, data in servers.items():
    plot_server_utilization(name, data)