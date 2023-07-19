#!/usr/bin/python3
"""
Reads input from stdin line by line and computes metrics.
"""

import sys


def print_statistics(total_file_size, status_counts):
    print(f"File size: {total_file_size}")
    sorted_status_codes = sorted(status_counts.keys())
    for status_code in sorted_status_codes:
        count = status_counts[status_code]
        print(f"{status_code}: {count}")


def parse_log_entry(log_entry):
    parts = log_entry.split()
    if len(parts) >= 7:
        status_code = parts[-2]
        file_size = int(parts[-1])
        return status_code, file_size
    else:
        return None, None


def compute_metrics(log_entries):
    total_file_size = 0
    status_counts = {}

    for log_entry in log_entries:
        status_code, file_size = parse_log_entry(log_entry)
        if status_code is not None and file_size is not None:
            total_file_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

    return total_file_size, status_counts


def read_logs():
    log_entries = []
    try:
        for line in sys.stdin:
            log_entries.append(line.strip())
            if len(log_entries) == 10:
                total_file_size, status_counts = compute_metrics(log_entries)
                print_statistics(total_file_size, status_counts)
                log_entries = []
    except KeyboardInterrupt:
        total_file_size, status_counts = compute_metrics(log_entries)
        print_statistics(total_file_size, status_counts)


if __name__ == "__main__":
    read_logs()

