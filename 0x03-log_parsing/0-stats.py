#!/usr/bin/python3
"""
File: 0-stats.py

Log parsing
"""
from collections import defaultdict
import sys
import re


def reporter(total_size, status_codes):
    """
    Prepares a report.

    parameters:
    - total_size (int): Size of a file.
    - status_codes (int): Status of a request.
    """
    print(f"File size: {total_size}")
    sorted_status_codes = sorted(status_codes.items())
    for status, count in sorted_status_codes:
        print(f"{status}: {count}")


def log_parser():
    """
    Reads stdin line by line and computes metrics.
    """
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]

    log_pattern = re.compile(r'^([\w\.-]+)\s*-?\s*\[([^\]]+)\] '
                             r'"GET /projects/260 HTTP/1\.1" (\S+) (\d+)$')

    try:
        for line in sys.stdin:
            if log_pattern.match(line):
                line_count += 1
                try:
                    file_size = int(line.split()[-1])
                    status_c = line.split()[-2]
                except ValueError:
                    continue

                total_size += file_size

                if status_c in codes:
                    status_codes[status_c] += 1

                if line_count == 10:
                    reporter(total_size, status_codes)
                    line_count = 0
            else:
                continue
        # One line report
        reporter(total_size, status_codes)
    except KeyboardInterrupt:
        reporter(total_size, status_codes)
        raise


if __name__ == "__main__":
    log_parser()
