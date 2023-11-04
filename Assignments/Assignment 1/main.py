import random
import queue

# توابع برای تولید زمان بین ورود مشتریان و زمان سرویس هر سرور
def generate_interarrival():
    rand = random.random()
    if rand < 0.20:
        return 1
    elif rand < 0.55:
        return 2
    elif rand < 0.70:
        return 3
    else:
        return 4

def generate_service_time_able():
    rand = random.random()
    if rand < 0.15:
        return 1
    elif rand < 0.40:
        return 2
    elif rand < 0.80:
        return 3
    else:
        return 4

def generate_service_time_baker():
    rand = random.random()
    if rand < 0.45:
        return 3
    elif rand < 0.75:
        return 4
    elif rand < 0.90:
        return 9
    else:
        return 11

# کلاس برای نگه داشتن اطلاعات سرور
class Server:
    def __init__(self, name):
        self.name = name
        self.end_time = 0
        self.queue = queue.Queue()
        self.idle_time = 0
        self.total_service_time = 0
        self.total_customers_served = 0

    # به‌روزرسانی زمان خالی بودن سرور
    def update_idle_time(self, current_time):
        if current_time >= self.end_time:
            self.idle_time += current_time - self.end_time

    # افزودن مشتری به صف و تنظیم زمان پایان سرویس
    def add_customer(self, customer, current_time):
        self.queue.put(customer)
        if current_time >= self.end_time:
            self.end_time = current_time + customer['service_time']
        else:
            self.end_time += customer['service_time']
        self.total_service_time += customer['service_time']
        self.total_customers_served += 1

    # محاسبه‌ی میانگین زمان سرویس دهی
    def average_service_time(self):
        return self.total_service_time / self.total_customers_served if self.total_customers_served else 0

    # محاسبه‌ی میانگین زمان خالی بودن
    def utilization(self, total_time):
        return 1 - (self.idle_time / total_time)

# تابع اصلی برای شبیه سازی
def simulate():
    current_time = 0
    total_simulation_time = 120  # مجموع زمان شبیه‌سازی به دقیقه

    # ایجاد دو سرور Able و Baker
    able = Server('Able')
    baker = Server('Baker')

    # متغیرهای برای محاسبه زمان انتظار
    total_wait_time = 0
    total_customers = 0

    while current_time < total_simulation_time:
        interarrival_time = generate_interarrival()
        current_time += interarrival_time

        service_time_able = generate_service_time_able()
        service_time_baker = generate_service_time_baker()

        able.update_idle_time(current_time)
        baker.update_idle_time(current_time)

        # انتخاب سرور برای سرویس دهی به مشتری جدید
        if able.end_time <= baker.end_time:
            able.add_customer({'arrival_time': current_time, 'service_time': service_time_able}, current_time)
            total_wait_time += max(0, able.end_time - current_time - service_time_able)
        else:
            baker.add_customer({'arrival_time': current_time, 'service_time': service_time_baker}, current_time)
            total_wait_time += max(0, baker.end_time - current_time - service_time_baker)

        total_customers += 1

    # محاسبه میانگین زمان انتظار
    average_wait_time = total_wait_time / total_customers if total_customers else 0

    print(f"Able Utilization: {able.utilization(total_simulation_time)}")
    print(f"Baker Utilization: {baker.utilization(total_simulation_time)}")
    print(f"Average Wait Time: {average_wait_time} minutes")
    print(f"Able Average Service Time: {able.average_service_time()} minutes")
    print(f"Baker Average Service Time: {baker.average_service_time()} minutes")
    print(f"Queue Length for Able: {able.queue.qsize()}")
    print(f"Queue Length for Baker: {baker.queue.qsize()}")

# اجرای تابع شبیه سازی
simulate()