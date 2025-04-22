import os
import psutil
import time
import platform

def get_size(bytes):
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

def monitor_system():
    print(f"Система: {platform.system()} {platform.version()}")
    print(f"Процессор: {platform.processor()}")

    print("\n--- Информация о процессоре ---")
    print(f"Нагрузка на процессор: {psutil.cpu_percent(interval=1)}%")
    print(f"Число ядер процессора: {psutil.cpu_count()} cores")

    print("\n--- Информация о памяти ---")
    memory = psutil.virtual_memory()
    print(f"Всего: {get_size(memory.total)}")
    print(f"Доступно: {get_size(memory.available)}")
    print(f"Используется: {get_size(memory.used)} ({memory.percent}%)")

    print("\n--- Информация о дисках ---")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Диск: {partition.device}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print(f"Всего: {get_size(partition_usage.total)}")
            print(f"Используется: {get_size(partition_usage.used)} ({partition_usage.percent}%)")
            print(f"Свободно: {get_size(partition_usage.free)}")
        except PermissionError:
            continue

    print("\n--- Информация о сети ---")
    net = psutil.net_io_counters()
    print(f"Всего отправлено байт: {get_size(net.bytes_sent)}")
    print(f"Всего получено байт: {get_size(net.bytes_recv)}")

if __name__ == "__main__":
    monitor_system()
