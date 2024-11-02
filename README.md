# Network Monitoring Script

## Description
This is a simple Python script that monitors the availability of multiple hosts or websites by pinging them at regular intervals. The script logs the status of each host to a log file and prints the results to the console. It is useful for basic network monitoring tasks to check if hosts are up or down.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/almamun-de/network-monitoring-script.git
   cd network-monitoring-script
   
Run the script:
python3 network_monitor.py

The script will start pinging the specified hosts and log the results to network_monitor_log.txt. The log file will be created in the same directory as the script.

Example
By default, the script monitors the following hosts:

8.8.8.8 (Google DNS)
google.com
192.168.1.1 (Local Router)
You can add or remove hosts by editing the hosts list in the script.

Notes
This script is for basic network monitoring. For more advanced monitoring, consider using dedicated tools like Nagios, Zabbix, or Prometheus.
The script logs the status of each host every 60 seconds by default. You can change the interval by modifying the interval variable.
