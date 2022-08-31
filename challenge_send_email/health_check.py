#! /usr/bin/env python3

import os
import shutil
import psutil
import socket
from emails import generate_error_report, send_email

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    print("CPU Usage: {:.2f}%".format(usage))
    return usage > 80

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print("Disk Free: {:.2f} %".format(free))
    return free > 20

def check_available_memory():
    available_memory = psutil.virtual_memory().available/(1024*1024)
    print("Available Virtual Memory: {:.2f} ".format(available_memory))
    return available_memory > 500

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

if check_cpu_usage():
    error_message = "CPU usage is over 80%"
elif not check_disk_usage('/'):
    error_message = "Available disk space is less than 20%"
elif not check_available_memory():
    error_message = "Available memory is less than 500MB"
elif not check_localhost():
    error_message = "localhost cannot be resolved to 127.0.0.1"
else:
    print("*** ALL HEALTH CHECKS PASSED ***")
    pass


if __name__ == "__main__":
    try:
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = "Error - {}".format(error_message)
        body = "Please check your system and resolve the issue as soon as possible"
        message = generate_error_report(sender, receiver, subject, body)
        send_email(message)
    except Exception as e:
        # set to pass - this means no error detected and no Email alert to be sent to you
        # if you suspect other error is encountered - just use:
        # print(e)
        pass
