import psutil
import logging
import time
import matplotlib.pyplot as plt
from collections import deque
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Device Monitoring Parameters
SENSORS = {
    "CPU Usage": lambda: psutil.cpu_percent(interval=1),
    "Memory Usage": lambda: psutil.virtual_memory().percent,
    "Temperature": lambda: psutil.sensors_temperatures().get('coretemp', [{}])[0].get('current', 0),
    "Fan Speed": lambda: psutil.sensors_fans().get('fan', [{}])[0].get('current', 0),
    "Device Health": lambda: 100 if psutil.disk_usage('/').percent < 85 else 50,
    "Interface Traffic": lambda: (psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv) / 1024
}

class RealTimeMultiDeviceMonitor:
    def __init__(self, max_data_points=60):
        self.device_data = {key: deque(maxlen=max_data_points) for key in SENSORS.keys()}
        self.timestamps = deque(maxlen=max_data_points)
        self.executor = ThreadPoolExecutor(max_workers=len(SENSORS))
    
    def fetch_data(self):
        """Fetches system monitoring data using multithreading."""
        try:
            future_tasks = {key: self.executor.submit(func) for key, func in SENSORS.items()}
            return {key: future.result() for key, future in future_tasks.items()}
        except Exception as e:
            logging.error(f"Error fetching system data: {e}")
            return None
    
    def update_data(self):
        """Fetch and update device monitoring data."""
        new_data = self.fetch_data()
        if new_data:
            for key in new_data:
                self.device_data[key].append(new_data[key])
            self.timestamps.append(time.strftime("%H:%M:%S"))
            logging.info(f"Updated device monitoring data: {new_data}")
        else:
            logging.warning("No new data received from system.")
    
    def generate_graphs(self):
        """Generates and updates real-time graphs for monitored data."""
        plt.clf()
        plt.figure(figsize=(12, 10))
        for i, (key, values) in enumerate(self.device_data.items(), 1):
            plt.subplot(3, 2, i)
            plt.plot(self.timestamps, list(values), marker='o', linestyle='-', label=key)
            plt.xlabel('Time')
            plt.ylabel(key)
            plt.title(f"{key} Over Time")
            plt.xticks(rotation=45)
            plt.legend()
        plt.tight_layout()
        plt.pause(1)
    
    def run(self, interval=1):
        """Continuously monitors device parameters and updates real-time graphs."""
        plt.ion()
        try:
            while True:
                self.update_data()
                self.generate_graphs()
                time.sleep(interval)
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
            plt.ioff()
            plt.show()

if __name__ == "__main__":
    monitor = RealTimeMultiDeviceMonitor()
    monitor.run()
