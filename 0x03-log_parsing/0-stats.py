#!/usr/bin/python3
import sys

total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

try:
    for line in sys.stdin:
        split_line = line.split()
        if len(split_line) >= 2:
            status_code = split_line[-2]
            file_size = split_line[-1]
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += int(file_size)
            line_count += 1
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print("{}: {}".format(code, count))
            print("")
except KeyboardInterrupt:
    pass

print("File size: {}".format(total_size))
for code, count in sorted(status_codes.items()):
    if count > 0:
        print("{}: {}".format(code, count))
