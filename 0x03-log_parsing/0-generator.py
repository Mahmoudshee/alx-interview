#!/usr/bin/python3
"""
Generates log entries in the specified format and writes them to stdout.
"""

import random
import sys
from time import sleep
import datetime


def generate_log_entry():
    ip_address = ".".join(str(random.randint(1, 255)) for _ in range(4))
    current_time = datetime.datetime.now()
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(1, 1024)

    return f"{ip_address} - [{current_time}] \"GET /projects/260 HTTP/1.1\" {status_code} {file_size}"


def generate_logs(num_entries):
    for _ in range(num_entries):
        sleep(random.random())
        log_entry = generate_log_entry()
        sys.stdout.write(f"{log_entry}\n")
        sys.stdout.flush()


if __name__ == "__main__":
    generate_logs(10000)

