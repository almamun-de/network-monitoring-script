import os
import time
import datetime

def ping_host(host):
    """
    Pings a single host and returns True if the host is reachable, False otherwise.
    """
    response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
    return response == 0

def monitor_hosts(hosts, interval, log_file):
    """
    Monitors a list of hosts at a specified interval. Logs the results to a file.
    """
    with open(log_file, 'a') as log:
        while True:
            for host in hosts:
                status = "up" if ping_host(host) else "down"
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_entry = f"{timestamp} - {host} is {status}\n"
                print(log_entry.strip())
                log.write(log_entry)
            time.sleep(interval)

