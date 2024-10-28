#!/usr/bin/python3

import sys

def main():
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    count_lines = 0

    try:
        for line in sys.stdin:
            count_lines += 1
            parts = line.split()
            
            # Validate the input format
            if len(parts) < 6:
                continue

            # Extract the file size and status code
            try:
                size = int(parts[-1])  # File size is the last part
                status_code = int(parts[-2])  # Status code is the second last part

                # Only process known status codes
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += size

            except ValueError:
                continue

            if count_lines % 10 == 0:
                print_stats(total_size, status_codes)
        
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

    print_stats(total_size, status_codes)

def print_stats(total_size, status_codes):
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

if __name__ == "__main__":
    main()
