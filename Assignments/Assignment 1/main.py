import random
import matplotlib.pyplot as plt

# تابعی برای تولید زمان سرویس بر اساس توزیع داده شده
def generate_service_time():
    rnd = random.random()
    if rnd < 0.1:
        return 0 + (1 - 0) * random.random()
    elif rnd < 0.5:
        return 1 + (2 - 1) * random.random()
    elif rnd < 0.9:
        return 2 + (3 - 2) * random.random()
    else:
        return 3 + (4 - 3) * random.random()

# تابعی برای تولید زمان بین ورودی‌ها بر اساس توزیع نمایی
def generate_interarrival_time():
    rate = 1.0 / 2.5
    return random.expovariate(rate)

# تعداد کل مشتریان
num_customers = 100

# زمان‌های بین ورود مشتریان و زمان ورود آنها
interarrival_times = [generate_interarrival_time() for _ in range(num_customers)]
arrival_times = [sum(interarrival_times[:i+1]) for i in range(num_customers)]

# متغیرهای مربوط به سرورها
servers = {
    'able': {'idle_time': 0, 'service_end': 0, 'utilization_times': []},
    'baker': {'idle_time': 0, 'service_end': 0, 'utilization_times': []}
}

# شبیه‌سازی
for i in range(num_customers):
    current_time = arrival_times[i]
    
    for server_name in servers:
        server = servers[server_name]
        if current_time >= server['service_end']:
            server['idle_time'] += current_time - server['service_end']
            service_time = generate_service_time()
            server['service_end'] = current_time + service_time
            server['utilization_times'].append((current_time, 1 - (server['idle_time'] / current_time)))
        else:
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

# ترسیم نمودارها برای هر سرور
for name, data in servers.items():
    plot_server_utilization(name, data)