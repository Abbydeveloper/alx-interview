#!/usr/bin/python3
"""
  Read stdin line by line and compute metrics
"""

import sys


def parse_log():
  """
    Store the file size and the HTTP status codes counts
    in a dictionary stdin_log
  """
  
  status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

  stdin_log = {"file_size": 0, "code_list": {str(code): 0 for code in status_codes}}

  return stdin_log

def print_code(log):
  """
    Print total file size, and the HTTP status codes count
    in a sorted order
  """

  print("File size: {}".format(log["file_size"]))

  sort_code = sorted(log["code_list"])

  for code in sort_code:
    if log["code_list"][code]:
      print(f"{code}: {log['code_list'][code]}")


def main():
  """
    Parse the stdin stream and return the total file size,
    as well as the count of HTTP status codes in a sorted order
  """

  log = parse_log()
  line_count = 0

  for line in sys.stdin:
    stdin_line = line.split()
    stdin_line = stdin_line[::-1]

    line_count += 1

    file_size = stdin_line[0]
    stat_code = stdin_line[1]
    
    log["file_size"] += int(file_size)

    if stat_code.isdecimal():
      log["code_list"][stat_code] += 1

    if line_count % 10 == 0:
      print_code(log)

if __name__ == "__main__":
  main()
